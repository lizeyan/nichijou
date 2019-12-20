# syntax = docker/dockerfile:1.0-experimental
FROM ubuntu:19.10
ARG PYTHON_VERSION=pypy3.6-7.2.0
ARG PIP_MIRROR=https://pypi.tuna.tsinghua.edu.cn/simple

ENV TZ 'Asia/Shanghai'
ENV LANG='C.UTF-8'
ENV LC_ALL='C.UTF-8'
ENV PYENV_ROOT=/root/.pyenv
ENV PATH="${PYENV_ROOT}/shims:${PYENV_ROOT}/bin:$PATH"

RUN  --mount=type=cache,target=/root/.cache echo '\
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ eoan main restricted universe multiverse \
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ eoan-updates main restricted universe multiverse \
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ eoan-backports main restricted universe multiverse \
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ eoan-security main restricted universe multiverse' > /etc/apt/sources.list && \
    apt-get update && apt-get install -y ca-certificates apt-transport-https && \
    echo '\
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ eoan main restricted universe multiverse \
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ eoan-updates main restricted universe multiverse \
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ eoan-backports main restricted universe multiverse \
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ eoan-security main restricted universe multiverse' > /etc/apt/sources.list && \
    DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        make build-essential libssl-dev zlib1g-dev libbz2-dev \
        libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
        xz-utils tk-dev libffi-dev liblzma-dev python-openssl git libblas-dev liblapack-dev \
        gfortran pybind11-dev zsh aria2 gcc gfortran python-dev libopenblas-dev liblapack-dev cython \
        graphviz libgraphviz-dev nodejs npm curl libhdf5-dev libxml2-dev libxslt1-dev && \
    curl -Lo install.sh https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh && \
    sh install.sh && \
    chsh -s /usr/bin/zsh && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN curl https://pyenv.run | bash && \
    printf 'export PATH="/root/.pyenv/bin:$PATH" \neval "$(pyenv init -)" \neval "$(pyenv virtualenv-init -)"\n' >> /root/.zshrc
# set pyenv done

RUN --mount=type=cache,target=/root/.cache --mount=type=cache,target=/root/.pyenv/cache aria2c https://github.com/squeaky-pl/portable-pypy/releases/download/${PYTHON_VERSION}/${PYTHON_VERSION}-linux_x86_64-portable.tar.bz2 -x 10 -k 1M --dir ~/.pyenv/cache/ && \
    pyenv install ${PYTHON_VERSION} && pyenv global ${PYTHON_VERSION}

## install python packages
RUN --mount=type=cache,target=/root/.cache/pip \
    pyenv versions && python --version && gcc --version && g++ --version && pip --version && \
    python -m pip install --upgrade pip -i ${PIP_MIRROR} && \
    pip install cython -i ${PIP_MIRROR} && \
    pip install numpy -i ${PIP_MIRROR} && \
    pip install -i ${PIP_MIRROR} tables && \
    pip install pandas -i ${PIP_MIRROR} && \
    pip install "scipy==1.3.3" -i ${PIP_MIRROR} && \
    pip install matplotlib -i ${PIP_MIRROR} && \
    pip install statsmodels -i ${PIP_MIRROR} && \
    pip install scikit-learn -i ${PIP_MIRROR} && \
    pip install -i ${PIP_MIRROR} \
           seaborn autopep8 jupyter plotly \
           jupyter_contrib_nbextensions \
           jupyterlab jupyter_nbextensions_configurator \
           loguru bidict coverage click dill pathos \
           joblib diskcache \
           networkx tqdm pygraphviz elasticsearch loguru pytest coverage visdom && \
    jupyter notebook --generate-config && \
    jupyter contrib nbextension install --system && \
    (pip uninstall -y pillow; CC="cc -mavx2" pip install -U -i ${PIP_MIRROR} --force-reinstall "pillow-simd==6.0.0.post0") && \
    jupyter nbextensions_configurator enable --system && \
    jupyter labextension install --no-build @jupyterlab/toc && \
    jupyter labextension install --no-build @telamonian/theme-darcula && \
    jupyter labextension install --no-build jupyterlab_vim && \
    jupyter labextension install --no-build jupyterlab-spreadsheet && \
    jupyter labextension install --no-build @aquirdturtle/collapsible_headings && \
    jupyter lab build

CMD ['zsh']
