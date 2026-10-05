"""Render one visual-review target as PNG only. Never calls the episode build."""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[1]
EP=ROOT/'episodes'/'imo_2017_p3'
TARGETS={
    'problem-opening':('reference_rebuilds.py','ProblemOpeningReference','problem_statement_opening_rebuild',None),
    'problem-initial':('reference_rebuilds.py','ProblemInitialReference','problem_statement_initial_rebuild',None),
    'problem-hunter':('reference_rebuilds.py','ProblemHunterReference','problem_statement_hunter_rebuild',None),
    'calibration':('style_calibration.py','StyleCalibration','style_calibration',None),
    'problem':('reference_rebuilds.py','ProblemStatementReference','problem_statement_reference_rebuild','problem_statement'),
    'problem-rules':('reference_rebuilds.py','ProblemRulesReference','problem_statement_rules_rebuild',None),
    'problem-tracking':('reference_rebuilds.py','ProblemTrackingReference','problem_statement_tracking_rebuild',None),
    'problem-question':('reference_rebuilds.py','ProblemQuestionReference','problem_statement_question_rebuild',None),
    'worlds':('reference_rebuilds.py','TwoWorldsReference','two_worlds_reference_rebuild','two_worlds'),
}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('target',choices=TARGETS)
    args=parser.parse_args()
    module,cls,stem,reference=TARGETS[args.target]
    media=EP/'media'/'visual_correction'
    out=EP/'output'
    out.mkdir(exist_ok=True)
    videos={p:(p.stat().st_size,p.stat().st_mtime_ns) for p in out.rglob('*.mp4')}
    command=[sys.executable,'-m','manim','--renderer','cairo','-s','--format','png',
             '-r','1920,1080','--media_dir',str(media),'-o',stem,str(EP/module),cls]
    log=out/f'{stem}.log'
    env=os.environ.copy()
    env['PYTHONIOENCODING']='utf-8'
    with log.open('w',encoding='utf-8') as handle:
        completed=subprocess.run(command,cwd=ROOT,env=env,stdout=handle,stderr=subprocess.STDOUT)
    if completed.returncode:
        raise RuntimeError(log.read_text(encoding='utf-8')[-3500:])
    source=media/'images'/Path(module).stem/f'{stem}.png'
    target=out/f'{stem}.png'
    shutil.copy2(source,target)
    with Image.open(target) as result:
        assert result.size==(1920,1080)
        if reference:
            polished=Image.open(EP/'references'/f'{reference}.png').convert('RGB')
            polished=polished.resize((1920,1080),Image.Resampling.LANCZOS)
            comparison=Image.new('RGB',(3840,1140),'#0D131D')
            comparison.paste(polished,(0,60)); comparison.paste(result,(1920,60))
            draw=ImageDraw.Draw(comparison)
            font=ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf',28)
            draw.text((36,10),'AUTHORITATIVE VISUAL REFERENCE',fill='#BBC5DB',font=font)
            draw.text((1956,10),'NEW MANIM RECONSTRUCTION · 1080p',fill='#BBC5DB',font=font)
            comparison.save(out/f'{reference}_comparison.png')
            # One display-size derivative; full-resolution comparison is retained.
            comparison.resize((1920,570),Image.Resampling.LANCZOS).save(out/f'{reference}_comparison_display.png')
    after={p:(p.stat().st_size,p.stat().st_mtime_ns) for p in out.rglob('*.mp4')}
    assert videos==after,'A video changed during a still-only task'
    print(json.dumps({'target':str(target),'resolution':[1920,1080],
                      'animations':0,'existing_videos_unchanged':True},indent=2))


if __name__=='__main__':
    main()
