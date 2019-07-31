#!/usr/bin/env bash

BUILD_ARGS=${@}
docker_exec=docker
tag=docker.peidan.me/lizytalk/nichijou:cp37_cpu
CONTEXT=$(realpath $(dirname "$0"))
sudo ${docker_exec} pull ${tag}
sudo ${docker_exec} build ${CONTEXT} ${BUILD_ARGS} -t ${tag}
sudo ${docker_exec} push ${tag}
