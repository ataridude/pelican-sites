Title: Telnetting via FujiNet
Date: 2021-6-14
Status: published

The [FujiNet](https://fujinet.online) is a very cool peripheral available for
8-bit Atari systems.

Somewhere along the way, I learned of the ability to telnet over the FujiNet.

The requirements are simple:

- A FujiNet device
- A terminal program
- Something to telnet into

For the first requirement, I have a FujiNet device.

For the second requirement, the terminal program can be found on the fujinet.online TNFS
server at /networking/modem-programs.atr.  As you can see, I mounted that image to drive 1 in the FujiNet
configuration on my Atari 800:

![FujiNet config](/images/fujinet-config.jpg)

For the third requirement, I added telnetd/xinetd to one of my Ubuntu VMs, and booted the Atari 800 into Ice-T XE.

To use telnet, you have to issue the `ATNET1` command to the FujiNet.  After that,
you use `ATDT` to telnet, such as `ATDT192.168.1.37` (or a hostname; DNS works as well):

![FujiNet telnet](/images/fujinet-telnet.jpg)

I think this is very cool -- I now can use my Atari 800 as an 80-column terminal connected
to my home network!
