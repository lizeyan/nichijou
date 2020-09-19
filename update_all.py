#!/usr/bin/env python3
from render import tag_kwargs
from subprocess import call
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

cwd = Path(__file__).parent

os.system("python render.py")

jobs = []
for tag, kwargs in tag_kwargs.items():
    jobs.append("cd {cwd}/{tag} && bash build-docker.sh".format(cwd=cwd, tag=tag, device=device))

with ThreadPoolExecutor(max_workers=10) as pool:
    pool.map(lambda job: call(job, shell=True), jobs)

jobs = ["cd {cwd}/visdom && bash build-docker.sh".format(cwd=cwd)]
with ThreadPoolExecutor(max_workers=10) as pool:
    pool.map(lambda job: call(job, shell=True), jobs)
