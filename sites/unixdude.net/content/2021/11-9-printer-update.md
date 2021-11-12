Title: Printer update
Category: Tech
Tags: docker, printer
Date: 2021-11-9
Status: published

Here's a months-overdue update on that [HP Envy printer](https://www.unixdude.net/posts/2021/Sep/07/docker-build/):  I wasn't able to
return the printer, and I still wanted a better
scanner app than the HP's built-in one, so I decided to take the
Raspberry Pi 4 that I mentioned in an earlier post and attach the printer
directly to it.  The goal of doing this was having better printing
than what I was doing before, where the printer was on my IoT VLAN,
and my print clients are all on my home VLAN.

In addition to having better printing functionality, I also wanted a better scanner app as I just mentioned. And, I wanted all of it working through [Traefik](https://traefik.io/traefik/), so that I can access the scanservjs app, printer admin page, and CUPS admin page all through Traefik.

As I mentioned, I got to learn about `docker build`, because there was no scanservjs image for ARM.  Fortunately, building for ARM is super fast on my M1 MacBook Air. I mean, my Intel iMac could build the ARM image too, but it takes a lot less time on my M1 MBA -- a minute or two on the M1 vs 1,000 seconds on the Intel, so I won't be building the ARM image on my iMac again!

I have now automated the build process mentioned in the earlier post: every now and again, I will pull the latest code from sbs20's scanservjs repo, then build it using his Dockerfile, with this script:

```
#!/bin/bash

IMAGE="ataridude/scanservjs"

[[ -z $1 ]] && echo "Usage: $0 tag" && exit -1
docker image build -t "${IMAGE}:$1" -t "${IMAGE}:latest" . && docker image push ${IMAGE}:$1 && docker image push ${IMAGE}:latest
```

I know there are ways to fully automate that `docker build` process, and I'll get to that point at some time,
but for now it's nice to have an easy way to update the image.

As you might expect, my Raspberry Pi print server is installed via [an Ansible playbook](https://github.com/ataridude/ansible/blob/master/playbook_print_server.yml).
I should look into the playbook and `docker-container-scanner` role, since this was the first Docker-oriented role I wrote, and I'm sure there is much that could be improved in the role and the playbook.
