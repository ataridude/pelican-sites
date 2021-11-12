Title: ESXi on ARM Fling - Update
Slug: esxi-on-arm-update
Category: Tech
Tags: virtualization, vmware
Date: 2021-4-20
Status: published

Not long after my last post, the PoE HAT for my Raspberry Pi died -- to be more accurate, one of the components
on the board disintegrated.  I don't know if this was a manufacturing defect or the result of a bad solder job
related to the fan, or something else.  In any case, disposed of that HAT and ordered the GeeekPi PoE HAT.  My
ESXi-on-ARM setup has been up and running since, connected by a single cable.

![Raspi 4](/images/raspi4.jpg)

I have this system booting from iSCSI, so there are no local filesystems -- the SD card is used only to initiate
the boot process, the system boots from iSCSI, and datastores are on the filer and are accessed via NFS.  I love
the elegance of this setup.

![ESX-ARM](/images/esxarm.jpg)

So far, I have created several VMs: Alpine, CentOS 8, Ubuntu, Raspberry Pi OS, and FreeBSD.  I haven't really
done much with any of this, but in my time with it so far I am impressed with its speed.  Speed-wise, it obviously doesn't
compare to my R610, but for about $100, it's great for what it is, and it makes an excellent geek toy.  And yes, I bought it mostly as a toy, but I do plan to
use it for some real-world services: In addition to general OS play, I plan to at least add a VM here to my [anycast DNS setup](<{filename}/2021/3-11-anycast.md>).

I might also build a VM on this server in order to relocate my UniFi controller.  I'm undecided
because I'm not sure how
much I like the problem that involves: if the raspi dies, so does my ability to run my controller. Solving this problem is important since I
currently run my UniFi controller in a VM that is hosted on my R610 and is NFS mounted.  I do need to find
another solution to the UniFi controller issue, since there are two switches between my R610 and my filer --
meaning that whenever I upgrade one of those switches, I have to reloate the controller VM to my iMac. This
is not how you should do it!

I haven't installed vSphere in a while, but now that I have two ESXi servers, I might do that again, so
that I can manage this entire setup more easily.
