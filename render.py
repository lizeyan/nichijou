#!/usr/bin/env python
import codecs
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

level1_tags = {
    'ubuntu20.04': {
        'base': 'ubuntu20.04',
        'pypi': 'https://mirrors.aliyun.com/pypi/simple/',
        'ubuntu': 'http://mirrors.tuna.tsinghua.edu.cn/ubuntu/',
        'python': 'https://npm.taobao.org/mirrors/python/',
        'docker_image': 'docker.peidan.me/lizytalk/nichijou',
        'group': "labmen",
        "group_id": "10000",
        "user": "lizytalk",
        "user_id": "10037",
    },
    'ubuntu18.04-cuda10.2': {
        'base': 'nvidia/cuda:10.2-devel-ubuntu18.04',
        'pypi': 'https://mirrors.aliyun.com/pypi/simple/',
        'ubuntu': 'http://mirrors.tuna.tsinghua.edu.cn/ubuntu/',
        'python': 'https://npm.taobao.org/mirrors/python/',
        'docker_image': 'docker.peidan.me/lizytalk/nichijou',
        'group': "labmen",
        "group_id": "10000",
        "user": "lizytalk",
        "user_id": "10037",
    },
    'ubuntu18.04-cuda9.2': {
        'base': 'nvidia/cuda:9.2-devel-ubuntu18.04',
        'pypi': 'https://mirrors.aliyun.com/pypi/simple/',
        'ubuntu': 'http://mirrors.tuna.tsinghua.edu.cn/ubuntu/',
        'python': 'https://npm.taobao.org/mirrors/python/',
        'docker_image': 'docker.peidan.me/lizytalk/nichijou',
        'group': "labmen",
        "group_id": "10000",
        "user": "lizytalk",
        "user_id": "10037",
    },
}

level2_tags = {
    'ubuntu18.04-cuda10.2-cp3.8.5': {
        'base': 'lizytalk/nichijou:ubuntu18.04-cuda10.2',
        'pypi': 'https://mirrors.aliyun.com/pypi/simple/',
        'ubuntu': 'http://mirrors.tuna.tsinghua.edu.cn/ubuntu/',
        'python': 'https://npm.taobao.org/mirrors/python/',
        'docker_image': 'docker.peidan.me/lizytalk/nichijou',
        'group': "labmen",
        "group_id": "10000",
        "user": "lizytalk",
        "user_id": "10037",
        "python_version": "3.8.5",
        "python_packages": "numba"
    },
    'ubuntu18.04-cuda9.2-cp3.5.10': {
        'base': 'lizytalk/nichijou:ubuntu18.04-cuda9.2',
        'pypi': 'https://mirrors.aliyun.com/pypi/simple/',
        'ubuntu': 'http://mirrors.tuna.tsinghua.edu.cn/ubuntu/',
        'python': 'https://npm.taobao.org/mirrors/python/',
        'docker_image': 'docker.peidan.me/lizytalk/nichijou',
        'group': "labmen",
        "group_id": "10000",
        "user": "lizytalk",
        "user_id": "10037",
        "python_version": "3.5.10"
    },
}

if __name__ == '__main__':

    source_root = Path(__file__).parent
    env = Environment(loader=FileSystemLoader(str(source_root.resolve())))

    for tag, kwargs in level1_tags.items():
        template = env.get_template('level1.template.dockerfile')
        output_dir = source_root / "{tag}".format(tag=tag)
        output_dir.mkdir(exist_ok=True)
        with codecs.open(str(output_dir / 'Dockerfile'), 'wb', 'utf-8') as f:
            f.write(template.render(**kwargs) + '\n')
        template = env.get_template('build-docker.sh.template')
        with codecs.open(str(output_dir / 'build-docker.sh'), 'wb', 'utf-8') as f:
            f.write(template.render(**kwargs, tag=tag) + '\n')

    for tag, kwargs in level2_tags.items():
        template = env.get_template('level2.template.dockerfile')
        output_dir = source_root / "{tag}".format(tag=tag)
        output_dir.mkdir(exist_ok=True)
        with codecs.open(str(output_dir / 'Dockerfile'), 'wb', 'utf-8') as f:
            f.write(template.render(**kwargs) + '\n')
        template = env.get_template('build-docker.sh.template')
        with codecs.open(str(output_dir / 'build-docker.sh'), 'wb', 'utf-8') as f:
            f.write(template.render(**kwargs, tag=tag) + '\n')
