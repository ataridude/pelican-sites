Title: Retiring my Dell R610
Date: 2021-12-22
Status: published

Ever since [a friend](https://mindlesstux.com/) gave me a Dell R610, I have used that as
my primary home lab server.  Due to its age, I find that I am unable to run the most 
recent versions of some software packages, including the latest iterations of VMware
ESXi and vCenter.  Also, my unit sits in a small room near the 3rd floor AC return in my house,
and this means that the heat it generates is pulled into the AC system, which affects my home's HVAC
operation.

For these and other reasons, I have decided to retire the R610 and replace it.  A while back,
I heard about [ServeTheHome's TinyMiniMicro project](https://www.servethehome.com/introducing-project-tinyminimicro-home-lab-revolution/), so I read some of their articles and decided to purchase a Lenovo M900 with an i7 CPU.  I upgraded my unit to 32GB RAM (the max), and this model includes vPro technology, which
is a plus or a minus depending on who you ask.  This unit will sit in my rack, rather
than on the floor leaning against the wall.  It will be a huge bonus that the M900 generates
less heat and uses less power than the R610.

My new M900 is much less capable overall than my R610: my R610 had a dual 300GB HDs in a
mirror, 192GB RAM, and dual Xeon 3.0 GHz for a total of 16 vCPUs.  The M900 has a single
256GB SSD, 32GB RAM, and a single 2.8GHz i7 CPU for a total of 8 vCPUs.  Even so, I think
this was a great purchase
based on my use case, which is to run ESXi and a dozen or so VMs.  Running vCSA 6, I maxed out on the R610 out at
40GB RAM usage, 10GB of which was vCSA -- so if I avoid vCSA, I'll stay below 30GB RAM usage.
Per-thread, the M900 is about 30% faster than the R610, so overall I think this is a huge win.

Having less RAM means I will have to be more selective about the VMs I run.  Fortunately, since this type of
setup is so cheap, if I need more capacity, I'll just buy another one of these 1L systems, be
it a Lenovo or a Dell or an HP.  So far, the M900 has exceeded my expectations.

Getting ESXi instsalled was an interesting experience: I couldn't get the M900 to boot from USB or PXE --
it seemed stuck on booting the included Windows installation.  I quickly learned the reason for this: the
M900 was configured for UEFI booting only; BIOS booting was disabled.  I enabled BIOS booting, downloaded the
Lenovo custom build of ESXi 7.0u2 and added it to my BIOS-only PXE setup, and started my install.  I was off
to the races, and so far I haven't found any issues with this build on this hardware.

After I got ESXi 7 installed on it, I installed vCSA 7, then added both the R610 and M900 to that vCenter
Server so I could use vMotion to migrate all of the VMs.  I had a few VMs on the local storage on the
R610 -- notably my UniFi Controller so that I can upgrade my Ubiquiti devices -- and it's so cool
that vCenter Server can migrate from local storage to local storage on different servers, without an intermediate
stop on a shared datastore.  Obviously 256-300GB space is not enough for many VMs; most of my VMs are
stored on NFS.

Another thing that really impressed me last night is that all of my VMs migrated without issue:
No complaints about CPU mismatch.  All VMs are now migrated, but I powered down a few of them
to save RAM.  With vCSA powered down, this system will be perfect for my needs:

![CPU/RAM Utilization](/images/m900/utilization.png)

I have a lot of cleanup to do here, but it's amazing how quiet and cool this area is, now that the R610
is powered down.

![M900 under rack](/images/m900/under-rack.jpeg)

The powered-down R610:

![R610](/images/m900/r610.jpeg)

The eBay seller did me right: this thing was super clean and looks practically new:

![front](/images/m900/front.jpeg)
![top](/images/m900/top.jpeg)
![inside](/images/m900/inside.jpeg)

One last thing: I have decided to convert my PXE setup to UEFI-only: at this point, I have zero need for
BIOS PXE booting, and UEFI will be better.  That will be an upcoming project.
