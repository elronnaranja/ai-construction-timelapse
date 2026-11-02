"""Integration checks: fail closed and exclude Flow's contaminated audio."""
import array
import importlib.util
import json
import math
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('assembler', ROOT / 'assemble.py')
assembler = importlib.util.module_from_spec(spec)
spec.loader.exec_module(assembler)


def ffmpeg(*args):
    subprocess.run(['ffmpeg', '-v', 'error', *args], check=True, capture_output=True)


class AudioDeliveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.directory = Path(cls.temp.name)
        cls.clip = cls.directory / 'flow.mp4'
        # 440 Hz models unwanted source music; 1000 Hz is the replacement marker.
        ffmpeg('-f', 'lavfi', '-i', 'color=c=gray:s=160x90:r=24:d=0.5',
               '-f', 'lavfi', '-i', 'sine=frequency=440:sample_rate=48000:duration=0.5',
               '-c:v', 'libx264', '-c:a', 'aac', str(cls.clip))
        cls.effect = cls.directory / 'effect.wav'
        ffmpeg('-f', 'lavfi', '-i', 'sine=frequency=1000:sample_rate=48000:duration=0.5', str(cls.effect))
        cls.hero = cls.directory / 'hero.png'
        ffmpeg('-f', 'lavfi', '-i', 'color=c=gray:s=160x90', '-frames:v', '1', str(cls.hero))
        cls.review = {
            'version': 1, 'method': 'listening', 'reviewed_by': 'synthetic integration fixture',
            'tracks': [{'clip_sha256': assembler.sha256(cls.clip),
                        'sfx_sha256': assembler.sha256(cls.effect), 'music_free': True,
                        'speech_free': True, 'scene_appropriate': True,
                        'rights': 'synthetic test signal; not production approval'} for _ in range(5)]}

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def save_review(self, review, name):
        path = self.directory / name
        path.write_text(json.dumps(review))
        return path

    def test_blocks_unapproved_audio(self):
        review = json.loads(json.dumps(self.review))
        review['tracks'][2]['music_free'] = False
        path = self.save_review(review, 'rejected.json')
        with self.assertRaisesRegex(ValueError, 'music_free'):
            assembler.validate_audio_review([self.clip]*5, [self.effect]*5, path)

    def test_blocks_changed_effect(self):
        review = json.loads(json.dumps(self.review))
        review['tracks'][0]['sfx_sha256'] = '0'*64
        path = self.save_review(review, 'stale.json')
        with self.assertRaisesRegex(ValueError, 'SFX changed'):
            assembler.validate_audio_review([self.clip]*5, [self.effect]*5, path)

    def test_blocks_raw_source_as_replacement(self):
        path = self.save_review(self.review, 'source.json')
        with self.assertRaisesRegex(ValueError, 'Flow source'):
            assembler.validate_audio_review([self.clip]*5, [self.clip]*5, path)

    def test_blocks_renamed_source_as_replacement(self):
        copied = self.directory / 'renamed-source.mp4'
        copied.write_bytes(self.clip.read_bytes())
        review = json.loads(json.dumps(self.review))
        for track in review['tracks']:
            track['sfx_sha256'] = assembler.sha256(copied)
        path = self.save_review(review, 'copied-source.json')
        with self.assertRaisesRegex(ValueError, 'copied Flow source'):
            assembler.validate_audio_review([self.clip]*5, [copied]*5, path)

    def test_missing_review_cannot_render(self):
        output = self.directory / 'must-not-exist.mp4'
        command = [sys.executable, str(ROOT/'assemble.py'), '--clips', *[str(self.clip)]*5,
                   '--hero', str(self.hero), '--output', str(output)]
        result = subprocess.run(command, capture_output=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(output.exists())

    def test_output_contains_effect_and_not_source_tone(self):
        path = self.save_review(self.review, 'approved-fixture.json')
        output = self.directory / 'output.mp4'
        command = [sys.executable, str(ROOT/'assemble.py'), '--clips', *[str(self.clip)]*5,
                   '--sfx-tracks', *[str(self.effect)]*5, '--audio-review', str(path),
                   '--hero', str(self.hero), '--output', str(output), '--aspect', '16:9', '--hold', '0.5']
        subprocess.run(command, check=True, capture_output=True)
        raw = subprocess.check_output(['ffmpeg', '-v', 'error', '-i', str(output), '-t', '0.4',
                                       '-vn', '-ac', '1', '-ar', '48000', '-f', 's16le', '-'])
        samples = array.array('h', raw)
        if sys.byteorder != 'little':
            samples.byteswap()
        def energy(frequency):
            real = sum(x*math.cos(2*math.pi*frequency*n/48000) for n,x in enumerate(samples))
            imag = sum(x*math.sin(2*math.pi*frequency*n/48000) for n,x in enumerate(samples))
            return math.hypot(real, imag)
        self.assertGreater(energy(1000), 15*energy(440))
        self.assertEqual(sum(s['codec_type']=='audio' for s in assembler.probe(output)['streams']), 1)


if __name__ == '__main__':
    unittest.main()
