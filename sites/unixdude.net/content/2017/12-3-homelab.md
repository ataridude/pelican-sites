Title: Home network/home lab
Slug: homelab
Category: Tech
Tags: nas, unix, esxi
Date: 2017-12-3
Status: published

I am frequently asked about my home network/home lab setup.  The summary is that I currently
use a Synology RT1900ac router, and two Synology NAS devices: a DS415+ as primary storage,
and a DS214se as backup.

For a number of years, I had a first-generation Drobo; later I added a
second generation Drobo S.  I liked those, but I wanted something
beefier and I wanted to switch from DAS to NAS.  I researched the
available options, and since I am a ZFS fan, I considered rolling my own server running FreeNAS.
I settled on Synology, in large part because of the user interface.

I sold the Drobos and bought a Synology DS415+ NAS, and today I use that
for my main storage.  My DS415+ is configured with 3x WD Red 3TB and 1x WD Red 4TB, in SHR;
this gives about 9TB of usable space.  I have a dozen or so NFS exports from the DS415+, and
three iSCSI LUNs.

All of my systems, both physical and virtual, are configured for the same user ID, and all Unix
systems use the NFS automounter.  My iMac also mounts the iSCSI LUNs, for things like
iMovie and iPhoto that require block-level storage.

Due to the size of the backup need, I chose a Synology as a backup device.  Since this is only for
backup, I chose a low-end DS214se; that unit is loaded with 2x WD Red 4TB configured as an 8TB JBOD.

When I first bought the DS415+, I moved data from my iMac's hard drive over to the NAS, but
that wasn't really fully utilizing it.  I later learned two things that completely changed my world:

* First, ESXi can be virtualized inside of VMware Fusion.  This was exciting because I did not have 
money or space for a virtualization lab -- but I did have an iMac with 32GB RAM in it.  I prefer
ESXi to Fusion for virtualization, but to that point had not been running ESXi at home, and was at
that time using Fusion for all of my virtualization needs.
* Second, ESXi can use NFS datastores. Fusion requires block-level storage, so I was excited to learn
that ESXi can use NFS storage.  (At this point, I was very new to ESXi administration.)

Ever since learning these two things about ESXi, I have run an ESXi server at home.  I started running
ESXi inside a VMware Fusion VM, and today that VM is running ESXi 6.5.0 Update 1. Eventually I would
like to migrate this to an Intel NUC, but for now it runs as a VM in VMware Fusion.  ESXi sees 10GB of RAM
and 2 out of my iMac's 4 CPUs.  I connect to my ESXi server two ways: either via Fusion Pro, or via
ESXi's built-in web client.

Back to the Synology: The Synology NAS can act as a PXE server, so I have configured pxelinux with a
menu that can boot several Linux distros, ESXi, and other things.  When I want to install an operating
system into a VM, I either use PXE, or I attach an ISO directly to the VM.

Nearly all of my virtualization has now been moved to ESXi.  I currently have more than 20 unique OSes
installed in VMs in ESX, mostly BSD variants or Linux distros.  In VMware Fusion, I run NeXTSTEP
3.3 and OPENSTEP 4.2; these do not seem to run in ESXi, and are the only OSes I run in Fusion anymore.
Well, other than ESXi itself, that is...

Once I do buy real hardware for it, the migration will be easy: I will install ESXi on the new
system, point it to the existing NFS exports, add the VMs, and start them up.
