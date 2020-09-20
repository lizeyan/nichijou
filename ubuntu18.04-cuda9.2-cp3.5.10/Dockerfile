# syntax = docker/dockerfile:1.0-experimental
FROM lizytalk/nichijou:ubuntu18.04-cuda9.2

ENV PATH="/homelizytalk/.pyenv/bin/:/usr/local/cuda/bin:/usr/bin/:${PATH}"
ENV LD_LIBRARY_PATH="/usr/lib/x86_64-linux-gnu:/usr/local/nvidia/lib64:/usr/local/nvidia/lib:/usr/local/cuda/lib64:/usr/local/cuda/lib:${LD_LIBRARY_PATH}"
ENV TZ=Asia/Shanghai
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ARG HOME=/home/lizytalk


USER lizytalk:labmen
WORKDIR /home/lizytalk

RUN --mount=type=cache,target=${HOME}/.cache/pip --mount=type=cache,target=${HOME}/.pyenv \
    zsh -c " \
    source ${HOME}/.zshrc && \
    aria2c https://npm.taobao.org/mirrors/python/3.5.10/Python-3.5.10.tar.xz -x 10 -k 1M --dir ${HOME}/.pyenv/cache/ && \
    pyenv install 3.5.10 && \
    pyenv global 3.5.10 && \
    pip install -U pip && \
    pip install numpy scipy statsmodels matplotlib seaborn pandas jupyter jupyterlab \
                jupyter_contrib_nbextensions jupyter_nbextensions_configurator \
                 && \
    jupyter notebook --generate-config && \
    jupyter contrib nbextension install --user && \
    jupyter nbextensions_configurator enable --user && \
    jupyter labextension install --no-build @jupyterlab/toc && \
    jupyter labextension install --no-build @telamonian/theme-darcula && \
    jupyter labextension install --no-build jupyterlab-spreadsheet && \
    jupyter labextension install --no-build @aquirdturtle/collapsible_headings && \
    jupyter lab build"

CMD ["/usr/bin/zsh"]

