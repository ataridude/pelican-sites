Title: Home lab
Date: 2024-5-26
Category: Homelab
Tags: homelab, esxi, synology, ubiquiti, raspberry pi, cisco
Status: published

I was recently asked about how to get started with a home lab.
As with most things, the answer depends on what you want to do
with it.  But, the core components are probably pretty similar.

Every home lab is going to require some sort of storage system.
For mine, I use Synology units running Btrfs.  I currently run
a DS1821+ as my primary storage unit, with 7 disks in an SHR-2
configuration, and one SSD cache disk.  I chose SHR-2 for its
RAID6-like double disk redundancy.  My disks are so large that
the likelihood of a second failure during a rebuild was high
enough that I wanted to protect against that.

I have a second Synology at home, a DS1618+, for backup purposes.
My first Synology sends Btrfs snapshots to the second.  This
backup unit uses SHR-2 like the primary, but with only 5 disks
in the array.

Most home labs will implement some sort of virtualization. For my
needs, free VMware ESXi on an i7-powered Lenovo M900 with 32GB RAM
works well.  I have tried Proxmox, and I greatly prefer ESXi.  I
know there are other solutions, and I will need to evaluate those
since Broadcom has done away with the free license, meaning home
lab users are out of luck with that one now.  When I had a Dell
R610 with 192GB RAM and was a member of VMUG, I ran vSphere, but
that takes too many resources on my M900.

I chose the M900 because at the time of my purchase, they were
readily available used on eBay for a couple hundred dollars, and
the i7 model supports 8 vCPUs and 32GB RAM.  Any of this type of
tiny server (there are many) should work.  My main recommendation
is to get an i7 and something that supports at least 32GB RAM.

For my network, I exclusively use Ubiquiti products.  I have
multiple sites and multiple VLANs.  I run OSPF and WireGuard to
connect those sites.  This is more than a beginner will need to do.

Other considerations:

* Backup power; I use a CyberPower 1500AVR.
* Monitoring; I run [Kuma](https://kuma.unixdude.net/status) for basic
monitoring

For additional reading, I recommend [Hayden James's excellent guide](https://linuxblog.io/home-lab-beginners-guide-hardware/).
