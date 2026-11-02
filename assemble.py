#!/usr/bin/env python3
"""Assemble Flow visuals with separately reviewed, music-free scene effects.
Flow audio is never mapped into the output. No audio review means no render.
"""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path


def probe(path):
    return json.loads(subprocess.check_output([
        'ffprobe', '-v', 'error', '-show_streams', '-show_format', '-of', 'json', str(path)
    ]))


def sha256(path):
    digest = hashlib.sha256()
    with path.open('rb') as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def validate_audio_review(clips, effects, review_path):
    review = json.loads(review_path.read_text())
    if review.get('version') != 1 or review.get('method') != 'listening':
        raise ValueError('Audio review must be version 1 and based on listening')
    if not str(review.get('reviewed_by', '')).strip():
        raise ValueError('A named audio reviewer is required')
    tracks = review.get('tracks', [])
    if len(tracks) != len(clips):
        raise ValueError('Review must cover all five clips in order')
    source_hashes = {sha256(clip) for clip in clips}
    for index, (clip, effect, track) in enumerate(zip(clips, effects, tracks), 1):
        if effect.resolve() in {c.resolve() for c in clips}:
            raise ValueError(f'Track {index}: Flow source cannot be used as an SFX track')
        if track.get('clip_sha256') != sha256(clip):
            raise ValueError(f'Track {index}: source clip changed since review')
        effect_hash = sha256(effect)
        if effect_hash in source_hashes:
            raise ValueError(f'Track {index}: copied Flow source cannot be used as SFX')
        if track.get('sfx_sha256') != effect_hash:
            raise ValueError(f'Track {index}: SFX changed since review')
        for field in ('music_free', 'speech_free', 'scene_appropriate'):
            if track.get(field) is not True:
                raise ValueError(f'Track {index}: {field} has not passed review')
        if not str(track.get('rights', '')).strip():
            raise ValueError(f'Track {index}: SFX usage rights must be recorded')
        if not any(s['codec_type'] == 'audio' for s in probe(effect)['streams']):
            raise ValueError(f'Track {index}: SFX file has no audio stream')
    return review


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--clips', nargs=5, required=True, type=Path)
    parser.add_argument('--hero', required=True, type=Path)
    parser.add_argument('--sfx-tracks', nargs=5, required=True, type=Path,
                        help='Five separate music-free effects tracks, one per clip')
    parser.add_argument('--audio-review', required=True, type=Path,
                        help='Listening review tied to clip and SFX SHA-256 hashes')
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--aspect', choices=['9:16', '16:9'], default='9:16')
    parser.add_argument('--hold', type=float, default=2.0)
    args = parser.parse_args()
    if not 0.5 <= args.hold <= 5:
        parser.error('--hold must be 0.5–5 seconds')
    for path in [*args.clips, args.hero, *args.sfx_tracks, args.audio_review]:
        if not path.is_file():
            parser.error(f'Missing file: {path}')
    if args.output.exists():
        parser.error('Output exists; use a new filename')
    try:
        review = validate_audio_review(args.clips, args.sfx_tracks, args.audio_review)
    except (ValueError, KeyError, TypeError) as error:
        parser.error(str(error))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    width, height = (720, 1280) if args.aspect == '9:16' else (1280, 720)
    command = ['ffmpeg', '-hide_banner', '-loglevel', 'error', '-n']
    for path in args.clips:
        command += ['-i', str(path)]
    command += ['-loop', '1', '-t', str(args.hold), '-i', str(args.hero)]
    for path in args.sfx_tracks:
        command += ['-i', str(path)]
    filters, durations = [], []
    for index, path in enumerate(args.clips):
        info = probe(path)
        video = next(s for s in info['streams'] if s['codec_type'] == 'video')
        duration = float(video.get('duration') or info['format']['duration'])
        durations.append(duration)
        filters.append(
            f'[{index}:v]scale={width}:{height}:force_original_aspect_ratio=decrease,'
            f'pad={width}:{height}:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=24,'
            f'format=yuv420p,trim=duration={duration},setpts=PTS-STARTPTS[v{index}]'
        )
        # Inputs 0–4 supply VISUALS ONLY. Inputs 6–10 are reviewed SFX.
        audio = (f'[{index+6}:a:0]aresample=48000,'
                 'aformat=sample_fmts=fltp:channel_layouts=stereo,'
                 f'apad,atrim=duration={duration},asetpts=PTS-STARTPTS')
        # Short edge fades reduce clicks; preserve the rest of each clip's sound.
        fade = min(0.04, duration / 4)
        audio += f',afade=t=in:st=0:d={fade}'
        tail = min(0.4 if index == 4 else fade, duration / 2)
        audio += f',afade=t=out:st={duration-tail}:d={tail}[a{index}]'
        filters.append(audio)
    filters.append(
        f'[5:v]scale={width}:{height}:force_original_aspect_ratio=decrease,'
        f'pad={width}:{height}:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=24,'
        f'format=yuv420p,trim=duration={args.hold},setpts=PTS-STARTPTS[v5]'
    )
    filters.append(f'anullsrc=r=48000:cl=stereo,atrim=duration={args.hold},'
                   'asetpts=PTS-STARTPTS[a5]')
    filters.append(''.join(f'[v{i}][a{i}]' for i in range(6)) +
                   'concat=n=6:v=1:a=1[outv][outa]')
    command += ['-filter_complex', ';'.join(filters), '-map', '[outv]', '-map', '[outa]',
                '-c:v', 'libx264', '-crf', '19', '-preset', 'fast', '-pix_fmt', 'yuv420p',
                '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', str(args.output)]
    subprocess.run(command, check=True)
    result = probe(args.output)
    video = next(s for s in result['streams'] if s['codec_type'] == 'video')
    if (video['width'], video['height']) != (width, height):
        raise RuntimeError('Unexpected output dimensions')
    if not any(s['codec_type'] == 'audio' for s in result['streams']):
        raise RuntimeError('Audio was not retained')
    subprocess.run(['ffmpeg', '-v', 'error', '-i', str(args.output), '-f', 'null', '-'], check=True)
    print(json.dumps({'output': str(args.output), 'audio_streams': 1,
                      'audio_review': 'passed listening review: ' + review['reviewed_by'],
                      'flow_audio_used': False,
                      'duration_seconds': float(result['format']['duration']),
                      'dimensions': [width, height], 'decode_check': 'passed'}, indent=2))


if __name__ == '__main__':
    main()
