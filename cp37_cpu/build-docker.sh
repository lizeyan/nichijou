#!/usr/bin/env bash

BUILD_ARGS=${@}
docker_exec=docker
tag=lizytalk/nichijou:cp37_cpu
CONTEXT=$(realpath $(dirname "$0"))
sudo ${docker_exec} pull ${tag}
sudo ${docker_exec} build ${CONTEXT} ${BUILD_ARGS} -t ${tag} --dns 101.6.6.6
sudo ${docker_exec} push ${tag}
