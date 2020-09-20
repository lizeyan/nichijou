#!/usr/bin/env bash

BUILD_ARGS=${@}
docker_exec=docker
tag=docker.peidan.me/lizytalk/nichijou:ubuntu18.04-cuda9.2-cp3.5.10
CONTEXT=$(realpath $(dirname "$0"))
sudo ${docker_exec} pull ${tag}
sudo ${docker_exec} build ${CONTEXT} ${BUILD_ARGS} -t ${tag} --network host
sudo ${docker_exec} push ${tag}
