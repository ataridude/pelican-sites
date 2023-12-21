Title: NFS automounter
Slug: nfs-automounter
Category: NFS
Tags: unix, nfs, synology, zerotier
Date: 2019-9-16
Status: published

In [an earlier post]({filename}2-20-scanner.md), I mentioned the NFS automounter.
I make use of the NFS automounter everywhere.  And by "everywhere," I mean "nearly every Unix system I install."
FreeBSD, NeXT systems, Mac OS X, Linux -- they all get the configuration.

The NFS automounter is useful because of the ease of use: if I need a file, I simply cd to the correct
location and use the file.

I install my automounts in /auto, so I cd to /auto/documents or /auto/downloads or whatever.  My ESXi server
uses files that on other systems are located under /auto/esx.

To make best use of this, I use the same user ID on all systems, and for security best practices, I set root squash
even though I'm the only user on the filer.

Also, because my filer is a Synology, I am able to share audio/video between iTunes and Synology's DS Audio/DS Video.
I do this by storing my iTunes library under /auto/media, and I set DS Audio and DS Video to use files found under
/volume1/media on the Synology.

The NFS filer is also useful remotely, because of [my use of ZeroTier]({filename}9-10-zerotier.md).  The NFS automounter,
with its automatic disconnects, works particularly well in this type of situation.
