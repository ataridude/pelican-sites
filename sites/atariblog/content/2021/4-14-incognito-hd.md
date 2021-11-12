Title: Incognito drive emulation
Slug: incognito-drive-emulation
Date: 2021-4-14
Status: published

A while ago, I bought the excellent Incognito for my 800 and installed it into
my system.  I have used it mostly for cartridge emulation, but recently my
children have started to program the 800 in Atari BASIC, so I needed to come up
with a better way to save programs than using my iPhone camera to take screenshots.

Having never used an Atari floppy before (as mentioned in an earlier post, I did
not have an Atari as a child and only bought my first one a few years ago), I did
not know how to do this.

Nothing here is advanced material, but I figure I'm not the only Atari newbie around,
and someone else might find this useful.  And, I'll find it useful the next time I 
need to do this job.

Fortunately, one of my friends is flashjazzcat over at [atari8.co.uk](https://atari8.co.uk).
He pointed me to his excellent [APT user manual](https://atari8.co.uk/wp-content/uploads/APT-Software-Manual-8th-Edition.pdf), and I used that to get this set up.

Here is what I did.

First, I configured the Incognito BIOS to emulate an XL/XE machine with 1MB RAM, and
set the system to boot DOS, with BASIC enabled:

![BIOS config](/images/fdisk-bios.jpeg)

Then I booted the system and ran FDISK:

![boot](/images/fdisk-boot.jpeg)

In FDISK, I divided my CF card into several partitions, and mounted those as separate
drives:

![drives](/images/fdisk-drives.jpeg)

After that, I exited FDISK, loaded BASIC, wrote a one-liner, saved it, exited back to
DOS, and printed a directory listing to see my file.

![file](/images/fdisk-file.jpeg)

Then I went back into BASIC, loaded the file, and listed it:

![basic](/images/fdisk-basic.jpeg)

Now my children can write and save all they want.

The reason I chose to start at D5: is because I wanted to reserve D1: to D4: for my
SDrive-MAX.  However, I will probably change this setup such that the Incognito
drives start at D1:.
