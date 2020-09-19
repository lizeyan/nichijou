#!/usr/bin/env bash

BUILD_ARGS=${@}
docker_exec=docker
tag=lizytalk/nichijou:cp36_cpu
CONTEXT=$(realpath $(dirname "$0"))
sudo ${docker_exec} pull ${tag}
sudo ${docker_exec} build ${CONTEXT} ${BUILD_ARGS} -t ${tag} --network host
sudo ${docker_exec} push ${tag}
