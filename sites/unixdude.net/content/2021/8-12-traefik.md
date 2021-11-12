Title: Traefik
Category: Tech
Date: 2021-8-12
Status: published

Lately I have been learning about Docker, and I want to convert my current setup to Docker,
where it makes sense to do that.  I currently run about 20 vhosts on this Digital Ocean droplet, and
at least one of those has a MySQL back end.  I also run Postfix/Dovecot/Sieve for mail.  And,
some other things run on here.

As part of my Docker studies, I was talking to a friend recently about my setup, and we were
discussing whether Docker is the right solution for the things I mentioned.  For now I'm
going to hold off on using Docker for my mail server, but I know there are some
container-based mail server solutions; I will look at those later, once I have migrated at least
some of the vhosts.

My friend and I started by discussing the vhosts I run.  Enter [Traefik](https://traefik.io), a free, Docker-
based and Docker-oriented proxy solution.  Even better: containers are automatically registered
with Traefik, and from what I have seen so far the only configuration necessary is to set some
tags on the containers as they are run, in your docker-compose file.

I decided to take one of my vhosts -- [www.ataridude.net](http://www.ataridude.net/) -- and run
it in/with Traefik.  I had some good success last night, and while it is not completely ready yet,
you can add this host entry to your system if you want to see it before it goes live:

    159.65.169.236 www.ataridude.net

To get this up and running, I built a docker-compose file based off of the one found in the
[Traefik quick-start](https://doc.traefik.io/traefik/getting-started/quick-start/):
```
version: '3'

services:
  reverse-proxy:
    # The official v2 Traefik docker image
    image: traefik:v2.4
    # Enables the web UI and tells Traefik to listen to docker
    command: --api.insecure=true --providers.docker
    ports:
      # The HTTP port
      - "80:80"
      # The Web UI (enabled by --api.insecure=true)
      - "8080:8080"
    volumes:
      # So that Traefik can listen to the Docker events
      - /var/run/docker.sock:/var/run/docker.sock

  atariblog:
    image: ataridude/private:atariblog
    labels:
      - "traefik.http.routers.atariblog.rule=Host(`www.ataridude.net`)"
```

The observant reader will note that the Traefik admin console is open and available.  Ordinarily this would not be a good idea,
but port 8080 is only available via ZeroTier (my Digital Ocean firewall configuration blocks port 8080), and if someone
joins my ZeroTier network, I have bigger issues than the Traefik admin console.

My blogs are Pelican-based, but I'm trying to get away from installing software on my systems,
at least as much as possible, so I decided to build the ataridude.net image using [Docker multi-
stage image builds](https://docs.docker.com/develop/develop-images/multistage-build/).  This
means I do not need Pelican or anything else installed on my server -- I only need Docker.

Here is the Dockerfile I'm using to build that image:
```
FROM python:3 AS builder
WORKDIR /usr/src/app

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
ADD content ./content
ADD theme ./theme
COPY pelicanconf.py ./
RUN pelican /usr/src/app/content/ -s pelicanconf.py

FROM nginx:latest

COPY --from=0 /usr/src/app/output /usr/share/nginx/html
```

I based this on my friend Brad's [Dockerfile](https://gitlab.com/blcarman/blog/-/blob/master/Dockerfile).

It's not as automated as I'd like, but it does work, and I will continue to improve it.

In addition to greater automation, I plan to start moving vhosts from my FreeBSD droplet over to a new Docker- and Ubuntu-based droplet.
