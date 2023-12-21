Title: General update
Slug: 2021-03-general-update
Category: Home lab
Tags: unix, ansible, pi-hole, raspberry pi
Date: 2021-3-10
Status: published

It has been a while since I did much of interest in the home lab, but that is changing this week.

I am starting to rework lots of things:

- This blog content is now tracked in a bitbucket repo
- I am upgrading my home network to UniFi hardware
- I am moving to an IaC setup

The first part was easy: create a repo, then push to it:
```
  git remote add origin git@bitbucket.org:unixdude/blog.git
  git push -u origin master
```

I should have done that a long time ago, but at least I had it tracked in a repo.  Now it is tracked in a
remote repo.  I will eventually migrate this server to Linux so that I can use containers; right now it runs
FreeBSD.

The second part comes after much consideration of what I wanted to do.  My 3-story house has many WiFi dead spots,
and I'm tired of that: it means that my Airport Express and Ring doorbell often don't work well.  I decided to go
with a UniFi setup, mostly for the single management pane and the ease of adding and upgrading hardware.  I should
have the new hardware sometime this week, and I hope to get it installed soon after I receive it.

Regarding the IaC setup, that is something several friends have done, and is something I should have done sooner.

I'm working toward having more cattle and fewer pets, and I'm working toward automated installs of that cattle.
I'm starting with Pi-Hole, which I use on a pet Raspberry Pi today.  When I'm done, Pi-Hole will be installed
on the raspi as well as a VM, and those two systems will share an IP address via anycast, so either one can go
down without affecting users on my network.

I'm also working toward using containers for things like Pi-Hole.  All of this will be installed and configured
via Ansible.

Speaking of Ansible, it is taking over some of the responsibilities of my PXE setup: my PXE setup now defaults to
a very basic install of Ubuntu 20.04.2 LTS, and Ansible will now be responsible for installing and configuring
packages such as NTP and other user- and system-configuration.
