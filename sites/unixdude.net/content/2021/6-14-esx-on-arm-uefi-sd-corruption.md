Title: June 2021 update
Category: Tech
Tags: vmware atari
Date: 2021-6-14
Status: published

I've been busy over the last few weeks, so there will be several updates in here.

-----

Over the weekend I updated my Ubiquiti switches, which required that I shut down my ESXi servers.  The
R610 came back just fine, but the raspi4 ARM one did not.  The problem on the Raspberry Pi was
the [known UEFI config corruption issue](https://github.com/pftf/RPi4/issues/104), when the UEFI config
is saved on the SD chip.

I thought maybe I would have to buy a new SD chip, but it turns out that only the RPI_EFI.fd file was
corrupt.  Unfortunately my previous blog posts did not serve their purpose -- I was not able to use them
to reinstall the Raspberry Pi ESXi ARM fling, and had to do all the research again, so:

- [ESXi on ARM installation howto](https://rudimartinsen.com/2020/10/07/esxi-on-arm-fling-install-on-rpi/) (there are many; this is the one I used last night)
- [ESXi on iSCSI on ARM](https://blogs.vmware.com/arm/2020/10/17/esxi-arm-with-iscsi/)

Since my SD chip was fine -- "diff -r" showed that only RPI_EFI.fd had changed since install -- I copied the
RPI_EFI.fd file to the SD chip, then booted the Raspberry pi.

I updated the EFI config as shown in step 3 of the install link above (the step which removes the 3GB RAM limit),
then I reconfigured the EFI to boot from iSCSI, as shown in the second link.  That post does not mention an issue
specific to Synology NASes, so I'll mention it here: when using a Synology NAS, the Boot LUN must be 1, not the
default of 0.

After that, I was able to boot my ESXi-on-ARM raspi again.  It is currently sitting on my desk,
and I'll probably leave it there, since I do not have remote console to it: with it on my desk, I can
easily connect a monitor and keyboard when needed.

-----

I decided I wanted to refresh my VMware skills, so I signed up for VMUG Advantage again about a week ago.  One
night last week I set up vCSA and then a cluster of 3 ESXi VMs.  VMware's unsupported-but-works-fine-in-a-lab
nested virtualization functionality is awesome, and I was feeling generous so I gave those 3 ESXi VMs 32GB and
8 vCPUs.  Since the R610 is not supported on v7 VMware products (the CPU is too old), I'm only running ESXi and
vCSA v6.7, but that's good enough for now.  It might be time to upgrade soon.

I put those nested ESXi VMs on my lab VLAN, and I have discovered an interesting issue: I cannot use Netboot.xyz
with VMs in that cluster.  I'm still trying to figure out why, but they just don't work.  The ESXi VMs are on
VLAN 7 (lab VLAN, 192.168.7.0/24), and any VM on that VLAN that is hosted directly on the R610 will PXE boot to
netboot.xyz without issue, and I can install any OS.  However, nested VMs (those running on the ESXi VMs) will
PXE boot to my menu, and can PXE boot local things, but they will not PXE boot netboot.xyz -- the netboot.xyz
menu loads, but no OS can be installed; see screenshot below.  Again, if I do exactly the same thing with
a VM on the R610, it works perfectly. Bizarre.

![Failed netboot.xyz install](/images/failed-netbootxyz-install.jpg)

-----

One specific reason for signing up for VMUG Advantuage again was that I want to play with NSX again, and to play
with vSAN for the first time.  Those are both upcoming projects.

-----

Another fun thing I did over the weekend was to telnet to an Ubuntu VM from my Atari 800.  There is a really cool
peripheral currently available for Atari 8-bit computers called the [FujiNet](https://fujinet.online), and using
a terminal program, one can use telnet.  I have [written up more on my Atari blog](https://www.ataridude.net/posts/2021/Jun/14/telnetting-via-fujinet/).
