from render import tag_kwargs
from subprocess import call
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

cwd = Path(__file__).parent

jobs = []
for device in ('cpu', 'gpu'):
    for tag, kwargs in tag_kwargs.items():
        jobs.append("cd {cwd}/{tag}_{device} && bash build-docker.sh".format(cwd=cwd, tag=tag, device=device))
jobs.append("cd {cwd}/visdom && bash build-docker.sh".format(cwd=cwd, tag=tag, device=device))

with ThreadPoolExecutor(max_workers=10) as pool:
    pool.map(lambda job: call(job, shell=True), jobs)
