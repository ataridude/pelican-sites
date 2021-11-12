Title: Update on migration to Docker/Traefik
Category: Tech
Tags: traefik, docker
Date: 2021-11-05
Status: published

I have been working hard these last many weeks in order to move all services off of my main DigitalOcean Droplet/VM.  In the process, I have been moving everything to Docker, with full automation via Ansible.  I have finally achieved this goal, for the web services anyway, and now I can deploy all of my web services with one or two Ansible commands: a bootstrap playbook (needed only for DigitalOcean VMs), and  a deploy playbook (good for VMs at home as well as ones at DigitalOcean).

I have uploaded my code [to GitHub](https://github.com/ataridude/ansible).  For DigitalOcean VMs, I start with [playbook_bootstrap.yml](https://github.com/ataridude/ansible/blob/master/playbook_bootstrap.yml), and for all VMs, I run [playbook_blog_server.yml](https://github.com/ataridude/ansible/blob/master/playbook_blog_server.yml).

This single command now sets up everything that used to be an Apache vhost on my main VM -- and all "vhosts" now run through [Traefik](https://traefik.io/traefik/).

This is a good milestone to reach, because it means I have now accomplished my goal of treating these services as "[infrastructure as code](https://en.wikipedia.org/wiki/Infrastructure_as_code)": I no longer make changes on the web server -- all changes are done in Ansible and/or Docker, then pushed out to the server.

Next up, I will work on moving my mail server (postfix, dovecot, spamassassin).

-----

While working on this project, one of the things I ran into is that the Pelican search plugin I have been using, [tipue_search](https://github.com/getpelican/pelican-plugins/tree/master/tipue_search), is no longer supported.  At first, this kept my main site on Apache, but eventually I decided I needed to get this sorted.  I made [my own copy of tipue_search](https://github.com/ataridude/pelican_tipue_search) and added it to the [Dockerfile](https://github.com/ataridude/unixdude.net/blob/master/Dockerfile) I am using to build this site, and now I have it working in my Dockerized blog implementation.  I had considered switching to the brand-new [pelican-algolia plugin](https://github.com/rehanhaider/pelican-algolia/tree/main/pelican/plugins/pelican_algolia), and while I still think that is a great solution I decided to stick with the tipue_search plugin I've been using for years.

-----

This Dockerfile uses a multi-stage build process, which I like because it lowers the requirements for my build server: the multi-stage build means that Pelican is not actually installed on my build server -- the entire build is done in a container.  I got this idea from a friend, who [does this with his blog](https://gitlab.com/blcarman/blog/-/blob/master/Dockerfile).

-----

Hopefully I will now find it easier to update this and my [Atari blog](https://www.ataridude.net).
