#!/usr/bin/env python3
from render import level1_tags, level2_tags
from subprocess import call
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import os

cwd = Path(__file__).parent

os.system("python render.py")

jobs = []
for tag, kwargs in level1_tags.items():
    jobs.append("cd {cwd}/{tag} && bash build-docker.sh".format(cwd=cwd, tag=tag))

for tag, kwargs in level2_tags.items():
    jobs.append("cd {cwd}/{tag} && bash build-docker.sh".format(cwd=cwd, tag=tag))

with ThreadPoolExecutor(max_workers=1) as pool:
    pool.map(lambda job: call(job, shell=True), jobs)
