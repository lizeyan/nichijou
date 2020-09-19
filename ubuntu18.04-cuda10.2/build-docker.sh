#!/usr/bin/env bash

BUILD_ARGS=${@}
docker_exec=docker
tag=lizytalk/nichijou:ubuntu18.04-cuda10.2_cpu
CONTEXT=$(realpath $(dirname "$0"))
sudo ${docker_exec} pull ${tag}
sudo ${docker_exec} build ${CONTEXT} ${BUILD_ARGS} -t ${tag} --network host
sudo ${docker_exec} push ${tag}
