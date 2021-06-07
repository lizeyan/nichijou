# syntax = docker/dockerfile:1.0-experimental
FROM ubuntu:20.04

ENV PATH="/usr/local/cuda/bin:${PATH}"
ENV LD_LIBRARY_PATH="/usr/lib/x86_64-linux-gnu:/usr/local/nvidia/lib64:/usr/local/nvidia/lib:/usr/local/cuda/lib64:/usr/local/cuda/lib:${LD_LIBRARY_PATH}"
ENV TZ=Asia/Shanghai
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV https_proxy="http://lzy-linux:8118"
ENV http_proxy="http://lzy-linux:8118"
ENV no_proxy="localhost,127.0.0.0/8,.svc,.default,.cluster.local,10.0.0.0/8,.domain.com,.local,dsb1,dsb2,dsb3,dsb4,dsb5,.0,.1,.2,.3,.4,.5,.6,.7,.8,.9,.10,.11,.12,.13,.14,.15,.16,.17,.18,.19,.20,.21,.22,.23,.24,.25,.26,.27,.28,.29,.30,.31,.32,.33,.34,.35,.36,.37,.38,.39,.40,.41,.42,.43,.44,.45,.46,.47,.48,.49,.50,.51,.52,.53,.54,.55,.56,.57,.58,.59,.60,.61,.62,.63,.64,.65,.66,.67,.68,.69,.70,.71,.72,.73,.74,.75,.76,.77,.78,.79,.80,.81,.82,.83,.84,.85,.86,.87,.88,.89,.90,.91,.92,.93,.94,.95,.96,.97,.98,.99,.100,.101,.102,.103,.104,.105,.106,.107,.108,.109,.110,.111,.112,.113,.114,.115,.116,.117,.118,.119,.120,.121,.122,.123,.124,.125,.126,.127,.128,.129,.130,.131,.132,.133,.134,.135,.136,.137,.138,.139,.140,.141,.142,.143,.144,.145,.146,.147,.148,.149,.150,.151,.152,.153,.154,.155,.156,.157,.158,.159,.160,.161,.162,.163,.164,.165,.166,.167,.168,.169,.170,.171,.172,.173,.174,.175,.176,.177,.178,.179,.180,.181,.182,.183,.184,.185,.186,.187,.188,.189,.190,.191,.192,.193,.194,.195,.196,.197,.198,.199,.200,.201,.202,.203,.204,.205,.206,.207,.208,.209,.210,.211,.212,.213,.214,.215,.216,.217,.218,.219,.220,.221,.222,.223,.224,.225,.226,.227,.228,.229,.230,.231,.232,.233,.234,.235,.236,.237,.238,.239,.240,.241,.242,.243,.244,.245,.246,.247,.248,.249,.250,.251,.252,.253,.254,.255"

# install software
RUN --mount=type=cache,target=/root/.cache/pip --mount=type=cache,target=/var/cache \
    printf "\
    deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse \n\
    deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-updates main restricted universe multiverse \n\
    deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-backports main restricted universe multiverse \n\
    deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-security main restricted universe multiverse \n\
    " > /etc/apt/sources.list && \
    ( rm /etc/apt/sources.list.d/nvidia-ml.list || echo "nvidia-ml.list not exist" ) && \
    ( rm /etc/apt/sources.list.d/cuda.list || echo "cuda.list not exist" ) && \
    DEBIAN_FRONTEND=noninteractive apt-get -y update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends ca-certificates &&\
    sed -i "s/http:\/\/mirrors\.tuna\.tsinghua\.edu\.cn\/ubuntu\//https:\/\/mirrors.tuna.tsinghua.edu.cn\/ubuntu\//g" /etc/apt/sources.list && \
    DEBIAN_FRONTEND=noninteractive apt-get -y update && \
    cat /etc/apt/sources.list && echo ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && \
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
        python-dev python-pip-whl libjpeg-dev htop sudo zsh liblapack-dev libatlas-base-dev ssh zookeeper \
        graphviz libgraphviz-dev curl thefuck direnv aria2 jq texlive \
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


ADD zsh-in-docker.sh /home/lizytalk/zsh-in-docker.sh
RUN sudo chown lizytalk:labmen /home/lizytalk/zsh-in-docker.sh

ADD pyenv.run /home/lizytalk/pyenv.run
RUN sudo chown lizytalk:labmen /home/lizytalk/pyenv.run



# install zsh
# Uses "git", "ssh-agent" and "history-substring-search" bundled plugins
RUN bash zsh-in-docker.sh \
    -p git -p ssh-agent -p 'history-substring-search' \
    -a 'bindkey "\$terminfo[kcuu1]" history-substring-search-up' \
    -a 'bindkey "\$terminfo[kcud1]" history-substring-search-down' \
    -t robbyrussell

# install pyenv and setup zshrc
RUN bash pyenv.run


ENV PATH=/home/lizytalk/.pyenv/bin:${PATH}

RUN (sed -i 's/source \$ZSH\/oh-my-zsh.sh/DISABLE_AUTO_UPDATE="true"\n\0/' ~/.zshrc) && \
    (printf '\neval "$(pyenv init --path)" \neval "$(pyenv init -)" \neval "$(pyenv virtualenv-init -)"\n' >> ~/.zshrc) && \
    (printf 'eval "$(direnv hook zsh)"' >> ~/.zshrc) && \
    zsh -c "pyenv versions"


CMD ["/usr/bin/zsh"]