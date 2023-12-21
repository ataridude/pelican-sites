Title: Lab update
Slug: lab_update
Category: Home lab
Tags: r610, pxe
Date: 2018-6-28
Status: published

As mentioned in [an earlier post](/posts/2017/Dec/03/homelab/), my ESXi server has been
running in a VMware Fusion VM on my iMac.  My iMac has 24 GB RAM and 4 logical CPUs; I 
dediated 10 GB RAM and 2 vCPUs to the ESXi VM.

Last week, I upgraded to a Dell R610 with 96GB RAM and dual Xeon 3 GHz CPUs (16 vCPUs).
Although ESXi 6.7 is unsupported on the R610, I installed it and so far it is working great.
I am really enjoying the breathing room that so many more CPUs and so much more RAM gives me.
Now I can create VMs pretty much as big as I would ever want.

I also made two changes to my PXE configuration.

First, I added a default boot option to the PXE config.  Now, it automatically
starts a CentOS 7 install after 10 seconds, complete with a kickstart file that adds my user and
installs my SSH keys.  Mere minutes after I boot a new VM, it is up and running
CentOS 7 and I can SSH into it.

Second, I updated my PXE environment to add [netboot.xyz](http://www.netboot.xyz/).
Previously I had the ability to install a half-dozen or so OSes via PXE.  Now I can install many more
OSes just as easily.

My next update will be to add a managed switch, so that I can use link aggregation
for my DS415+ and R610.
