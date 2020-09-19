# syntax = docker/dockerfile:1.0-experimental
FROM nvidia/cuda:10.2-devel-ubuntu18.04

ENV PATH="/usr/local/cuda/bin:${PATH}"
ENV LD_LIBRARY_PATH="/usr/lib/x86_64-linux-gnu:/usr/local/nvidia/lib64:/usr/local/nvidia/lib:/usr/local/cuda/lib64:/usr/local/cuda/lib:${LD_LIBRARY_PATH}"
ENV TZ=Asia/Shanghai
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

# install software
RUN --mount=type=cache,target=/root/.cache/pip --mount=type=cache,target=/var/cache \
    sed -i "s/http:\/\/archive\.ubuntu\.com\/ubuntu\//https:\/\/mirrors.tuna.tsinghua.edu.cn\/ubuntu\//g" /etc/apt/sources.list && \
    sed -i "s/http:\/\/security\.ubuntu\.com\/ubuntu\//https:\/\/mirrors.tuna.tsinghua.edu.cn\/ubuntu\//g" /etc/apt/sources.list && \
    cat /etc/apt/sources.list && echo ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && \
    DEBIAN_FRONTEND=noninteractive apt-get -y update && \
    DEBIAN_FRONTEND=noninteractive apt-get -y dist-upgrade && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        locales language-pack-en tzdata ca-certificates lsb-release iputils-ping \
        apt-utils apt-transport-https gnupg dirmngr openssl software-properties-common  \
        tar wget ssh git mercurial vim openssh-client psmisc rsync \
        build-essential autoconf libtool \
        libssl-dev zlib1g-dev libncurses5-dev libncursesw5-dev libreadline-dev libsqlite3-dev \
        libgdbm-dev libdb5.3-dev libbz2-dev libexpat1-dev liblzma-dev tk-dev \
        libnlopt-dev libpq-dev libffi-dev libcairo-dev libedit-dev \
        libcurl4-nss-dev libsasl2-dev libsasl2-modules libapr1-dev libsvn-dev \
        python-dev python-pip libjpeg-dev htop sudo zsh liblapack-dev libatlas-base-dev ssh zookeeper \
        graphviz libgraphviz-dev curl thefuck direnv \
    && \
    (curl -sL https://deb.nodesource.com/setup_14.x | bash) && \
    sed -i "s/https:\/\/deb\.nodesource\.com\/node\//https:\/\/mirrors.tuna.tsinghua.edu.cn\/nodesource\/deb\//g" /etc/apt/sources.list.d/nodesource.list && \
    DEBIAN_FRONTEND=noninteractive apt-get -y update && \
    DEBIAN_FRONTEND=noninteractive apt-get -y install nodejs && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN groupadd -g 10000 labmen && \
    useradd -g labmen -u 10037 lizytalk && \
    mkdir /home/lizytalk && chown lizytalk:labmen /home/lizytalk &&\
    echo "lizytalk		ALL = (ALL) NOPASSWD: ALL" >> /etc/sudoers

USER lizytalk:labmen
WORKDIR /home/lizytalk

# install zsh
# Uses "git", "ssh-agent" and "history-substring-search" bundled plugins
RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.1/zsh-in-docker.sh)" -- \
    -p git -p ssh-agent -p 'history-substring-search' \
    -a 'bindkey "\$terminfo[kcuu1]" history-substring-search-up' \
    -a 'bindkey "\$terminfo[kcud1]" history-substring-search-down' \
    -t robbyrussell

# install pyenv
RUN curl https://pyenv.run | bash && \
    printf 'export PATH="/home/lizytalk/.pyenv/bin:$PATH" \neval "$(pyenv init -)" \neval "$(pyenv virtualenv-init -)"\n' >> ~/.zshrc
# set pyenv done


CMD ["/usr/bin/zsh"]
