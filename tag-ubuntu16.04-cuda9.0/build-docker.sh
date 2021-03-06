#!/usr/bin/env bash

BUILD_ARGS=${@}
docker_exec=docker
tag=docker.peidan.me/lizytalk/nichijou:ubuntu16.04-cuda9.0
CONTEXT=$(realpath $(dirname "$0"))
sudo ${docker_exec} pull ${tag}
sudo ${docker_exec} build ${CONTEXT} ${BUILD_ARGS} -t ${tag} --network host --progress=plain
sudo ${docker_exec} push ${tag}
