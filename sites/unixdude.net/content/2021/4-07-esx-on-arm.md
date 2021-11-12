Title: ESXi on ARM Fling
Slug: esxi-on-arm-fling
Category: Tech
Tags: virtualization, vmware
Date: 2021-4-07
Status: published

I recently decided that I wanted to play with the [ESXi-on-ARM Fling](https://flings.vmware.com/esxi-arm-edition), so
I purchased a [Raspberry Pi 4B](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/) (8GB).
I received my unit so I set about installing ESXi.

I followed VMware's instructions in their "Fling-on-Raspberry-Pi" document.  It's not a difficult
process, but there are a few things to note about the process found in that document.

One of the first steps is to update the Raspberry Pi's EEPROM; VMware's document says to
use the Raspberry Pi Imager to flash an SD chip with the "Raspberry Pi EEPROM boot recovery" utility,
but I found this to not be available in the Imager utility.  With a little help from my favorite search engine, I found
[the official documentation on updating the boot EEPROM](https://www.raspberrypi.org/documentation/hardware/raspberrypi/booteeprom.md),
which includes commands to do it from a running instance of Raspberry Pi OS.  With that I was able
to confirm that my raspi is up-to-date.

One thing to note is that the official PoE HAT is not supported (at least, not out of the box), because
its fan is controlled by the I2C, which is nonfunctional when running ESXi.  Unfortunately for me, I did
not know about this limitation before buying the official PoE HAT; I chose to solve this problem by
soldering leads from pins 4 & 6 on the GPIO directly to the fan -- I want the fan to always run anyway,
so that is a fine solution for me.

The main use for a micro SD chip is to configure the UEFI, so don't buy a large one.  In my experience,
the micro SD chip is also your main boot device (without one inserted, my unit won't boot).  Also, you
need a USB drive on which to install ESXi.  NFS datastores are supported, so I am mounting those from
my NAS.  I use one datastore for installation ISOs, and one for VMs.

I am looking into installing ESXi on an iSCSI LUN but so far I have not been able to get that
to work with my Synology: the Raspberry Pi connects (I see this on the Synology), but the LUN does not
show up in the device list on the raspi.

Be sure to follow the instructions on configuring the NTP client, since it works differently than an
x86_64 ESXi server does.

So far I have installed Ubuntu 20 and CentOS 8.  This is looking like a great little toy!
