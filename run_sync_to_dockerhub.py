from render import level1_tags, level2_tags
from subprocess import call


for key, tags in list(level1_tags.items()) + list(level2_tags.items()):
    source = tags["docker_image"]
    target = "/".join(source.split("/")[-2:])
    print(f"sync {source}:{key} to {target}:{key}")
    call(f"docker tag {source}:{key} {target}:{key} && docker push {target}:{key}", shell=True)

