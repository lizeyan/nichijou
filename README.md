## About this docker
Install python and common used packages: numpy, scipy, pytorch, matplotlib, tensorflow...
Built images at Docker Hub: https://cloud.docker.com/repository/docker/lizytalk/nichijou
``` bash
docker pull lizytalk/nichijou:{tag}
```
## Build this docker
1. change the parameters in render.py
2. `python render.py`
3. `docker build {{ tag }}`
4. [optional] `bash setup-env.sh`
## Tags
|tags|description|
|---|---|
|cp36_cpu|Ubuntu 18.04 CPython 3.6|
|cp37_cpu|Ubuntu 18.04 CPython 3.7|
|cp36_gpu|Ubuntu 18.04 CPython 3.6, CUDA 10.0, CUDNN 7|
|cp37_gpu|Ubuntu 18.04 CPython 3.7, CUDA 10.0, CUDNN 7|
|visdom|Based on cp37_cpu, run visdom server|
