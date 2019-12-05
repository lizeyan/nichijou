#!/usr/bin/env python
import codecs
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

tag_kwargs = {
    'cp36': {
        'users': [{'uid': 10037, 'username': 'lizytalk'}, ],
        'gid': 10000,
        'group_name': 'labmen',
        'jupyter_container': 'lzy-jupyter',
        'pypi': 'https://mirrors.aliyun.com/pypi/simple/',
        'ubuntu': 'http://mirrors.tuna.tsinghua.edu.cn/ubuntu/',
        'python': 'https://npm.taobao.org/mirrors/python/',
        'docker_image': 'lizytalk/nichijou',
        'python_major_version': '3.6',
        'python_version': '3.6.9',
        "code_server": 'code-server1.1156-vsc1.33.1-linux-x64',
    },
    'cp37': {
        'users': [{'uid': 10037, 'username': 'lizytalk'}, ],
        'gid': 10000,
        'group_name': 'labmen',
        'jupyter_container': 'lzy-jupyter',
        'pypi': 'https://mirrors.aliyun.com/pypi/simple/',
        'ubuntu': 'http://mirrors.tuna.tsinghua.edu.cn/ubuntu/',
        'python': 'https://npm.taobao.org/mirrors/python/',
        'docker_image': 'lizytalk/nichijou',
        'python_major_version': '3.7',
        'python_version': '3.7.5',
        "code_server": 'code-server1.1156-vsc1.33.1-linux-x64',
    },
    'cp38': {
        'users': [{'uid': 10037, 'username': 'lizytalk'}, ],
        'gid': 10000,
        'group_name': 'labmen',
        'jupyter_container': 'lzy-jupyter',
        'pypi': 'https://mirrors.aliyun.com/pypi/simple/',
        'ubuntu': 'http://mirrors.tuna.tsinghua.edu.cn/ubuntu/',
        'python': 'https://npm.taobao.org/mirrors/python/',
        'docker_image': 'lizytalk/nichijou',
        'python_major_version': '3.8',
        'python_version': '3.8.0',
        "code_server": 'code-server1.1156-vsc1.33.1-linux-x64',
    },
}

if __name__ == '__main__':

    source_root = Path(__file__).parent
    env = Environment(loader=FileSystemLoader(str(source_root.resolve())))

    for tag, kwargs in tag_kwargs.items():
        for name in ('cpu', 'gpu'):
            template = env.get_template('Dockerfile.template')
            output_dir = source_root / "{tag}_{name}".format(tag=tag, name=name)
            output_dir.mkdir(exist_ok=True)
            with codecs.open(str(output_dir / 'Dockerfile'), 'wb', 'utf-8') as f:
                f.write(template.render(gpu=(name == 'gpu'), **kwargs) + '\n')
            template = env.get_template('nichijou.template')
            with codecs.open(str(output_dir / 'nichijou'), 'wb', 'utf-8') as f:
                f.write(template.render(gpu=(name == 'gpu'), **kwargs, tag=tag) + '\n')
            template = env.get_template('build-docker.sh.template')
            with codecs.open(str(output_dir / 'build-docker.sh'), 'wb', 'utf-8') as f:
                f.write(template.render(gpu=(name == 'gpu'), **kwargs, tag=tag) + '\n')
            template = env.get_template('nichijou-jupyter.template')
            with codecs.open(str(output_dir / 'nichijou-jupyter'), 'wb', 'utf-8') as f:
                f.write(template.render(gpu=(name == 'gpu'), **kwargs, tag=tag) + '\n')
