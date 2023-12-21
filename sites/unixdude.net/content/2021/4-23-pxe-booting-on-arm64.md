Title: PXE booting on ARM64
Slug: pxe-booting-on-arm64
Category: Home lab
Tags: virtualization, vmware, pxe, home lab
Date: 2021-4-23
Status: published

As previously mentioned, my next goal was going to be PXE booting VMs running on the
ESXi ARM Fling.  Using [this page](https://discourse.ubuntu.com/t/netbooting-the-live-server-installer-via-uefi-pxe-on-arm-aarch64-arm64-and-x86-64-amd64/19240) as a guide, I now have this working.

That guide is pretty good, but I had to do adapt it to my setup.

As instructed, I started by downloading the grub EFI binary and installing that
on my TFTP server, at `tftp.unixdude.net/grubnetaa64.efi.signed`.

I updated my [USG](https://store.ui.com/products/unifi-security-gateway) to add a new IP subnet and VLAN
for the ARM64 VMs, so that I could set up a PXE configuration specifically for those VMs, without
affecting the PXE setup I have for x64 systems.  Yes, if I ran my own DHCP server, I could have added
configuration to it to detect the client architecture and to have it send the correct boot code based
on that.  This way was easy, and it has the benefit of not affecting my home network in the case that the DHCP
server VM is down. (High WAF in the network not going down.)

On the new subnet, I specify the DNS server (my [anycast IP address](<{filename}/2021/3-11-anycast.md>)), and
I point the "DHCP network boot" options to my TFTP server, with a boot filename of `/grubnetaa64.efi.signed`.
I also specify the DHCP TFTP Server IP address.

On the filer, I extracted the `grub.cfg`, `initrd`, and `vmlinuz` files as instructed.  Initially
I tried putting those files into a `/arm64` directory on my filer, but that did not work for me, so
I moved them to the root directory and was able to PXE boot the VM right away.

I added the `grub.cfg` entry as indicated, modifying it to point to my local copy of the
Ubuntu image.

After that, I booted the VM.  The first time I booted it, I ran out of memory because
I had only given the VM 1GB of RAM.  I increased that to 4GB (half the memory of the raspi)
and was able to successfully PXE boot a VM and install Ubuntu.

![arm-pxe2](/images/arm-pxe2.png)
![arm-pxe4](/images/arm-pxe4.png)

I consider this a success despite its impracticality: I cannot realistically PXE boot VMs if
I have to dedicate half the server's memory in order to do it.
