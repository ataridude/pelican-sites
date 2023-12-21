Title: ECMP in OSPF
Date: 2022-2-20
Category: Networking
Tags: ospf, routing, ecmp, wireguard, zerotier, usg, digitalocean
Status: published

I have recently switched most of my offsite network connections to
WireGuard, away from ZeroTier.  This is great for all of my systems
except for one: the NAS (a Synology DS118) I have at a friend's house
for offsite backup.  That NAS can run ZeroTier and WireGuard, but
I don't know of any dynamic routing protocol options for it, so I can
have only a single WireGuard connection rather than the two I want.
My solution here is to create a ZeroTier network between that NAS and
the two VMs I have at DigitalOcean.  For my purposes, that is close
enough to having two WireGuard links and the ability to route to
both of them.

Another issue I wanted to resolve was the CPU load on my USG: with
WireGuard running on the USG, high traffic utilization on the WireGurad
links results in
100% CPU load on the USG, and that slows everything down.  The solution there was to
add WireGuard links from my Pi-Hole systems at home to my DigitalOcean
VMs, and to increase the OSPF link cost from the USG to the DigitalOcean
VMs.  As long as my USG is up, I'll have connectivity to my DOVMs,
but if one of my Pi-Hole systems is up, I will have better connectivity
to the DOVMs.

I also wanted to set all of this up with redundant links and ECMP such
that any link can be down, and have everything continue to work.

Below is a current network diagram.  The offsite links are WireGuard with
the exception of the ZeroTier network (shown in green) that connects the two DOVMs and
the NAS.  (The two DOVMs are of course also connected by a WireGuard link.)
A single OSPF area is used throughout, for all of the routing.

This has been an enjoyable project, and a great learning experience.

![network](/images/complete_network_2022-02.jpg)
