#syntax=docker/dockerfile-upstream:master-experimental
FROM {{ base }}

ENV PATH="/home{{ user }}/.pyenv/bin/:/usr/local/cuda/bin:/usr/bin/:${PATH}"
ENV LD_LIBRARY_PATH="/usr/lib/x86_64-linux-gnu:/usr/local/nvidia/lib64:/usr/local/nvidia/lib:/usr/local/cuda/lib64:/usr/local/cuda/lib:${LD_LIBRARY_PATH}"
ENV TZ=Asia/Shanghai
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ARG HOME=/home/{{ user }}


USER lizytalk:labmen
WORKDIR /home/{{ user }}

RUN --mount=type=cache,uid={{ user_id }},target=/home/{{ user }}/.cache/pip --mount=type=cache,target=/home/{{ user }}/.pyenv/cache \
    sudo chown -R lizytalk /home/{{ user }}/.cache/pip && sudo chown -R lizytalk /home/{{ user }}/.pyenv/cache && \
    zsh -c " \
    source ${HOME}/.zshrc && \
    aria2c https://npm.taobao.org/mirrors/python/{{ python_version }}/Python-{{ python_version }}.tar.xz -x 10 -k 1M --dir ${HOME}/.pyenv/cache/ && \
    pyenv install {{ python_version }} && \
    pyenv global {{ python_version }} && \
    pip install -U pip && \
    pip install numpy scipy statsmodels matplotlib seaborn pandas jupyter jupyterlab \
                jupyter_contrib_nbextensions jupyter_nbextensions_configurator \
                {{ python_packages }} && \
    jupyter notebook --generate-config && \
    jupyter contrib nbextension install --user && \
    jupyter nbextensions_configurator enable --user && \
    jupyter labextension install --no-build @jupyterlab/toc && \
    jupyter labextension install --no-build @telamonian/theme-darcula && \
    jupyter labextension install --no-build jupyterlab-spreadsheet && \
    jupyter labextension install --no-build @aquirdturtle/collapsible_headings && \
    jupyter lab build"

CMD ["/usr/bin/zsh"]

