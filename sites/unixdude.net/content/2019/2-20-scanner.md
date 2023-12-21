Title: Scanner
Slug: scanner
Category: General
Tags: unix, scanner, raspberry pi, nfs, synology
Date: 2019-2-20
Status: published

I own a CanoScan LiDE 30.  This scanner is about 15 years old, and back
when I got it new, it was supported on Mac OS X.  Canon stopped updating
the drivers a couple years later, so I switched to [TWAIN-SANE](http://www.ellert.se/twain-sane/).

When I did that, I wrote a "scan" shell script that uses scanimage to
grab a TIFF from the scanner, and then mogrify (part of ImageMagick) to
convert the TIFF to JPEG.  My scan script saves scans to an NFS automounted
directory, so it doesn't matter what computer I scan with, I just happened
to do it on my iMac.  Or my MacBook Pro - it didn't matter.

Unfortunately, Mattias stopped updating his drivers a few years ago, so
I wanted to find another way to use my perfectly good LiDE 30.

I own a Raspberry Pi 3, and I knew that the TWAIN-SANE drivers that Mattias
used were simply ports of the open source Linux counterparts, so I installed
the SANE and ImageMagick packages on my Raspi and used that for scanning.  I
used the same scan script that I had on the Mac, and with the NFS
automount, everything worked as it had before.

Until this week, that is, when I relocated my Raspi to my living room to connect it
to my TV.

Once again, I was looking for a scanning solution.  I can't use my Macs (the only
computers in my office).  My R610 is in my garage, which is not convenient to
scanning.  I don't want to carry my scanner to the living room to connect to the
Raspi, so what can I do?

The answer is easy: I run a single FreeBSD VM on my Synology DS1618+.  A quick search, and I
discovered sane-backends and sane-fronends are ported to FreeBSD.  The question
remained: Can my Synology connect a USB page scanner to one of its VMs, and will
that work properly?  In mere moments, I had the SANE packages and ImageMagick
installed on the Synology-hosted FreeBSD VM.  And, moments later, I was scanning
successfully using exactly the same script I started with on the iMac a decade ago.

Ah, the magic of open source and NFS automounts.

The FreeBSD port has some problems, but it's fine as long as I don't run "scanimage -L" --
that crashes the VM, either a full lockup or a kernel panic and reboot.  But, since
my scanner works with scanimage, that's all I care about.  I just avoid the "-L" parameter,
and all is well.
