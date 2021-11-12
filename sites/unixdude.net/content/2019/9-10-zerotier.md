Title: Home Network update 2019-09
Slug: home-network-update-2019-09
Category: Tech
Tags: network
Date: 2019-9-10
Status: published

My home network has changed significantly in recent months.

First, I purchased three MikroTik devices, an [RB260GS](https://mikrotik.com/product/RB260GS) for my office and two
[hAP AC](https://mikrotik.com/product/RB962UiGS-5HacT2HnT), one for my office and one for my garage.  This allowed
me to simplify my network and it provides for several changes.  My network now looks like this:

![Home network 2019](/images/home_network_2019.jpg)

As a result, I can upgrade the Synology RT1900ac without taking down my entire home network. I can upgrade the
office switch or hAP AC without affecting my family's network access, and updates to the garage hAP AC will only
affect my R610-based home lab.

-----

A while ago I was introduced to [Zerotier](http://www.zerotier.com/).  I gave it
a look and found an extremely useful networking solution.  To use it, one need only do a few simple things:

* Create a Zerotier login

* Create a network

* Install the software on your systems/devices

* Join those systems/devices to your network

* Approve the join requests (if your network is private)

The [Zerotier admin UI](https://my.zerotier.com/) shows the IP addresses of each system, and it allows the
user to set a nickname for each device.

Using this solution, I was able to completely disable global SSH access to all of my systems:
now, the only way to SSH to my systems is to be on my Zerotier network or my home network.

-----

I created a services VM that sits on both ZeroTier and my home network; this VM forwards packets between
ZeroTier and my home network, so with a few simple routes added to a few devices, I can now access my entire home
network from anywhere:

* Synology RT1900ac has routes to the Zerotier subnet (via the services VM) and the lab subnet (via the hAP AC in the garage)
* My laptop has routes to the home and lab subnets, via the services VM

-----

macOS has long had a very cool feature where you can use per-domain DNS servers, so I use my home-based DNS
servers to resolve *.unixdude.net no matter where I am.  This, coupled with these new routes, allows me to
resolve everything at home by hostname, and to connect to it.  This is immensely useful.
