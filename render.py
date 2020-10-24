#!/usr/bin/env python
import codecs
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from jinja2 import Environment, FileSystemLoader
import os


files = [
    {
        "name": "zsh-in-docker.sh",
        "url": "https://github.com/deluan/zsh-in-docker/releases/download/v1.1.1/zsh-in-docker.sh"
    },
    {"name": "pyenv.run", "url": "https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer"},
]


level1_tags = {
    'ubuntu18.04-cuda10.2': {
        'base': 'nvidia/cuda:10.2-cudnn7-devel-ubuntu18.04',
        'pypi': 'https://mirrors.aliyun.com/pypi/simple/',
        'ubuntu': 'http://mirrors.tuna.tsinghua.edu.cn/ubuntu/',
        'python': 'https://npm.taobao.org/mirrors/python/',
        'docker_image': 'docker.peidan.me/lizytalk/nichijou',
        'group': "labmen",
        "group_id": "10000",
        "user": "lizytalk",
        "user_id": "10037",
        "template": "ubuntu18.level1.template.dockerfile",
    },
    'ubuntu16.04-cuda9.0': {
        'base': 'nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04',
        'pypi': 'https://mirrors.aliyun.com/pypi/simple/',
        'ubuntu': 'http://mirrors.tuna.tsinghua.edu.cn/ubuntu/',
        'python': 'https://npm.taobao.org/mirrors/python/',
        'docker_image': 'docker.peidan.me/lizytalk/nichijou',
        'group': "labmen",
        "group_id": "10000",
        "user": "lizytalk",
        "user_id": "10037",
        "template": "ubuntu18.level1.template.dockerfile",
    },
    'ubuntu18.04': {
        'base': 'ubuntu:18.04',
        'pypi': 'https://mirrors.aliyun.com/pypi/simple/',
        'ubuntu': 'http://mirrors.tuna.tsinghua.edu.cn/ubuntu/',
        'python': 'https://npm.taobao.org/mirrors/python/',
        'docker_image': 'docker.peidan.me/lizytalk/nichijou',
        'group': "labmen",
        "group_id": "10000",
        "user": "lizytalk",
        "user_id": "10037",
        "template": "ubuntu18.level1.template.dockerfile",
    }
}

level2_tags = {
    'ubuntu18.04-cuda10.2-cp3.8.5': {
        'base': 'docker.peidan.me/lizytalk/nichijou:ubuntu18.04-cuda10.2',
        'pypi': 'https://mirrors.aliyun.com/pypi/simple/',
        'ubuntu': 'http://mirrors.tuna.tsinghua.edu.cn/ubuntu/',
        'python': 'https://npm.taobao.org/mirrors/python/',
        'docker_image': 'docker.peidan.me/lizytalk/nichijou',
        'group': "labmen",
        "group_id": "10000",
        "user": "lizytalk",
        "user_id": "10037",
        "python_version": "3.8.5",
        "python_packages": "numba",
        "template": "level2.template.dockerfile",
    },
    'ubuntu16.04-cuda9.0-cp3.5.10': {
        'base': 'docker.peidan.me/lizytalk/nichijou:ubuntu16.04-cuda9.0',
        'pypi': 'https://mirrors.aliyun.com/pypi/simple/',
        'ubuntu': 'http://mirrors.tuna.tsinghua.edu.cn/ubuntu/',
        'python': 'https://npm.taobao.org/mirrors/python/',
        'docker_image': 'docker.peidan.me/lizytalk/nichijou',
        'group': "labmen",
        "group_id": "10000",
        "user": "lizytalk",
        "user_id": "10037",
        "python_version": "3.5.10",
        "template": "level2.template.dockerfile",
    },
    'ubuntu18.04-cp3.8.5': {
        'base': 'docker.peidan.me/lizytalk/nichijou:ubuntu18.04',
        'pypi': 'https://mirrors.aliyun.com/pypi/simple/',
        'ubuntu': 'http://mirrors.tuna.tsinghua.edu.cn/ubuntu/',
        'python': 'https://npm.taobao.org/mirrors/python/',
        'docker_image': 'docker.peidan.me/lizytalk/nichijou',
        'group': "labmen",
        "group_id": "10000",
        "user": "lizytalk",
        "user_id": "10037",
        "python_version": "3.8.5",
        "template": "level2.template.dockerfile",
    },
}


def render(tag, kwargs):
    template = env.get_template(kwargs["template"])
    output_dir = source_root / "tag-{tag}".format(tag=tag)
    output_dir.mkdir(exist_ok=True)
    with codecs.open(str(output_dir / 'Dockerfile'), 'wb', 'utf-8') as f:
        f.write(template.render(**kwargs, files=files) + '\n')
    template = env.get_template('build-docker.sh.template')
    with codecs.open(str(output_dir / 'build-docker.sh'), 'wb', 'utf-8') as f:
        f.write(template.render(**kwargs, files=files, tag=tag) + '\n')


if __name__ == '__main__':

    source_root = Path(__file__).parent
    env = Environment(loader=FileSystemLoader(str(source_root.resolve())))

    with ThreadPoolExecutor(max_workers=10) as pool:
        pool.map(render, *zip(*level1_tags.items()))
    with ThreadPoolExecutor(max_workers=10) as pool:
        pool.map(render, *zip(*level2_tags.items()))

