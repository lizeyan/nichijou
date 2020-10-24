#!/usr/bin/env python3
from render import level1_tags, level2_tags, files
from subprocess import call
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import os
import sys


def download_file(config):
    os.system(f"curl -L {config['url']} -o {cwd}/{config['name']}")


def delete_file(config):
    os.system(f"rm {cwd}/{config['name']}")


cwd = Path(__file__).parent

os.system("python render.py")

jobs = []
for tag, kwargs in level1_tags.items():
    jobs.append(
        "cd {cwd}/tag-{tag} && \
        cp {_src} . && \
        bash build-docker.sh {args} && \
        rm {_dst} ".format(
            cwd=cwd, tag=tag, args=" ".join(sys.argv[1:]),
            _src=' '.join('../' + item['name'] for item in files),
            _dst=' '.join(item['name'] for item in files),
        )
    )

for tag, kwargs in level2_tags.items():
    jobs.append(
        "cd {cwd}/tag-{tag} && \
        cp {_src} . && \
        bash build-docker.sh {args} && \
        rm {_dst} ".format(
            cwd=cwd, tag=tag, args=" ".join(sys.argv[1:]),
            _src=' '.join('../' + item['name'] for item in files),
            _dst=' '.join(item['name'] for item in files),
        )
    )

with ThreadPoolExecutor(max_workers=10) as pool:
    pool.map(download_file, files)

with ThreadPoolExecutor(max_workers=1) as pool:
    pool.map(lambda job: call(job, shell=True), jobs)

with ThreadPoolExecutor(max_workers=10) as pool:
    pool.map(delete_file, files)
