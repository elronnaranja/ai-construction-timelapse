#!/usr/bin/env python3
"""Assemble five ordered clips plus approved hero hold, with guaranteed no audio."""
import argparse,json,subprocess
from pathlib import Path

def run(args): return subprocess.run(args,check=True)

def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('--clips',nargs=5,required=True,type=Path)
 p.add_argument('--hero',required=True,type=Path)
 p.add_argument('--output',required=True,type=Path)
 p.add_argument('--aspect',choices=['9:16','16:9'],default='9:16')
 p.add_argument('--hold',type=float,default=2.0)
 a=p.parse_args()
 if not 0.5<=a.hold<=5: p.error('--hold must be 0.5–5 seconds')
 for f in [*a.clips,a.hero]:
  if not f.is_file(): p.error(f'missing file: {f}')
 if a.output.exists(): p.error(f'output exists: {a.output}; use a new filename')
 a.output.parent.mkdir(parents=True,exist_ok=True)
 w,h=(720,1280) if a.aspect=='9:16' else (1280,720)
 cmd=['ffmpeg','-hide_banner','-loglevel','error','-n']
 for f in a.clips: cmd+=['-i',str(f)]
 cmd+=['-loop','1','-t',str(a.hold),'-i',str(a.hero)]
 filt=[]
 for i in range(6):
  filt.append(f'[{i}:v]scale={w}:{h}:force_original_aspect_ratio=decrease,pad={w}:{h}:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=24,format=yuv420p,setpts=PTS-STARTPTS[v{i}]')
 filt.append(''.join(f'[v{i}]' for i in range(6))+'concat=n=6:v=1:a=0[out]')
 cmd+=['-filter_complex',';'.join(filt),'-map','[out]','-an','-c:v','libx264','-crf','19','-preset','fast','-pix_fmt','yuv420p','-movflags','+faststart',str(a.output)]
 run(cmd)
 info=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(a.output)]))
 if any(s['codec_type']=='audio' for s in info['streams']): raise RuntimeError('Audio stream found')
 v=next(s for s in info['streams'] if s['codec_type']=='video')
 if (v['width'],v['height'])!=(w,h): raise RuntimeError('Wrong dimensions')
 run(['ffmpeg','-v','error','-i',str(a.output),'-f','null','-'])
 print(json.dumps({'output':str(a.output),'duration_seconds':float(info['format']['duration']),'width':w,'height':h,'audio_streams':0,'decode_check':'passed'},indent=2))
if __name__=='__main__': main()
