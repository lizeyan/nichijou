#!/usr/bin/env bash

BUILD_ARGS=${@}
docker_exec=nvidia-docker
tag=lizytalk/nichijou:cp38_gpu
CONTEXT=$(realpath $(dirname "$0"))
sudo ${docker_exec} pull ${tag}
sudo ${docker_exec} build ${CONTEXT} ${BUILD_ARGS} -t ${tag}
sudo ${docker_exec} push ${tag}
