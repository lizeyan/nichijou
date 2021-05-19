#syntax=docker/dockerfile-upstream:master-experimental
FROM docker.peidan.me/lizytalk/nichijou:ubuntu18.04-cuda10.2

ENV PATH="/homelizytalk/.pyenv/bin/:/usr/local/cuda/bin:/usr/bin/:${PATH}"
ENV LD_LIBRARY_PATH="/usr/lib/x86_64-linux-gnu:/usr/local/nvidia/lib64:/usr/local/nvidia/lib:/usr/local/cuda/lib64:/usr/local/cuda/lib:${LD_LIBRARY_PATH}"
ENV TZ=Asia/Shanghai
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ARG HOME=/home/lizytalk
ARG PY_VERSION=3.9.4


USER lizytalk:labmen
WORKDIR /home/lizytalk

RUN --mount=type=cache,uid=10037,target=/home/lizytalk/.cache/pip --mount=type=cache,target=/home/lizytalk/.pyenv/cache \
    sudo chown -R lizytalk /home/lizytalk/.cache/pip && sudo chown -R lizytalk /home/lizytalk/.pyenv/cache && \
    zsh -c " \
    pyenv versions && \
    aria2c https://npm.taobao.org/mirrors/python/${PY_VERSION}/Python-${PY_VERSION}.tgz -x 10 -k 1M --dir ${HOME}/.pyenv/cache/ && \
    pyenv install ${PY_VERSION} && \
    pyenv global ${PY_VERSION}"

RUN --mount=type=cache,uid=10037,target=/home/lizytalk/.cache/pip --mount=type=cache,target=/home/lizytalk/.pyenv/cache \
    zsh -c "\
    source ~/.zshrc && \
    pyenv versions && pyenv which pip && \
    pip install -U pip && \
    pip install -U xeus-python && \
    pip install numpy scipy statsmodels matplotlib seaborn pandas jupyter jupyterlab \
                jupyter_contrib_nbextensions jupyter_nbextensions_configurator \
                 && \
    jupyter notebook --generate-config && \
    jupyter contrib nbextension install --user && \
    jupyter nbextensions_configurator enable --user && \
    jupyter lab build"

CMD ["/usr/bin/zsh"]

