#!/usr/bin/env bash
IMAGE_NAME=docker.peidan.me/lizytalk/nichijou:pypy3.6_cpu
sudo docker build --progress=plain . -t ${IMAGE_NAME} --network host
sudo docker push ${IMAGE_NAME}