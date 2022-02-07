Title: Lab update
Date: 2022-1-31
Category: Networking
Tags: update, docker, portainer, T1, homelab, ubiquiti, usg, wireguard, rack
Status: published

I have been hard at work these last few weeks in my home lab, and have done quite a bit.  Here are a
few of the things I have done:

* Installed [sshwifty](https://github.com/nirui/sshwifty), a really cool, useful
package that a friend pointed me to.
* Built a [T1 crossover cable](https://www.freeccnaworkbook.com/blog/ccna/how-to-make-a-t1-crossover) to connect the two routers I have in my home lab that have a T1 CSU/DSU WIC installed.
* Installed [Portainer](https://www.portainer.io) on my production Docker Swarm
* Renumbered my home network from 192.168.1.0/24 to 192.168.8.0/24.  I undertook this effort because
I have a NAS hosted at a friend's house, and his network also uses the 192.168.1.0/24 address space, so
that made it difficult for me to get to my NAS -- sure, I could get to it, but every system that needed
access to it needed to be on my ZeroTier storage network.  Now, I can route directly to it, and return
packets are routed to my network instead of to his.
* Deployed WireGuard extensively, using FRR, OSPF, and Anycast to access systems.  Because of
CPU utilization issues I discovered after doing this, I might move my WireGuard routing/endpoint to my raspberry pi or to a VM in order to work around those issues.
* Added more monitoring under [Kuma](https://kuma.unixdude.net/status).
* Deployed a new NAS, a [Synology DS220+](https://www.synology.com/en-us/products/DS220+) to take some load off my DS1618+ and to use it as cold storage.
* Through the generosity of a friend, I have replaced my three Cisco 2950s with two 2960-Xs and one 3750G.
* I have finished racking all my devices.
* I have cabled up my Cisco lab again.  I have also connected the lab to my home network via my
[Ubiquiti USG](https://store.ui.com/products/unifi-security-gateway)'s
LAN2 port, so that I can route to it.  I have console access to all of the devices, using [a 4-port
USB-to-serial adapter](https://www.amazon.com/Gearmo-Serial-Windows-Certified-Drivers/dp/B004ETDC8K/)
and some mini USB cables (for the 2960s) connected to my Raspberry Pi, but I also want network access.
 The current lab setup, which will hopefully be useful for much learning, is shown here:

![lab network](/images/lab-network-2022-01.jpg)

* I installed a patch panel, which cleaned up the rack a bit.  Here are before & after pics.  Because
my switch and router are not rack-mount devices, it's not as clean as it could be, but I still think
this came out very well.

![before](/images/patch-panel/before.jpeg)

![after](/images/patch-panel/after.jpeg)

Next up:

* Configure the newly recabled Cisco lab.
* Finish migrating data to the DS220+.
* Clean up the power and ethernet cables behind and below the rack.
