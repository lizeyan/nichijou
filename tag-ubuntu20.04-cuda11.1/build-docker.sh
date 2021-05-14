#!/usr/bin/env bash

BUILD_ARGS=${@}
docker_exec=docker
tag=docker.peidan.me/lizytalk/nichijou:ubuntu20.04-cuda11.1
CONTEXT=$(realpath $(dirname "$0"))
sudo ${docker_exec} pull ${tag}
sudo ${docker_exec} build ${CONTEXT} ${BUILD_ARGS} -t ${tag} --network host --progress=plain
sudo ${docker_exec} push ${tag}
