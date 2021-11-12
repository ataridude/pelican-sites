Title: Blog automation
Category: Tech
Tags: docker, ansible
Date: 2021-9-26
Status: published

This is a short post after a lot of work.

I have been busy these last few weeks automating the installation of [Docker](https://www.docker.com),
[Traefik](https://traefik.io/traefik/), and [my Atari blog](https://www.ataridude.net) with [Ansible](https://www.ansible.com/).
I have reached the point that I can take a fresh install of Ubuntu 20.04 LTS and end up with a
completely functional blog server.  The "fresh install" requires only my user, SSH key, and passwordless
sudo configuration... once I have that, Ansible takes care of everything else.  I simply run
```ansible-playbook playbook_blog_server.yml``` ... et voila.

Now to work on correcting some of the things I did wrong here, and moving the unixdude.net blog into a
Docker container behind Traefik.

For those who are interested, I have [pushed the code](https://github.com/ataridude/ansible).
