Title: Mounting disks with FujiNet web interface
Date: 2021-7-14
Status: published

I have [mentioned it before](/posts/2021/Jun/14/telnetting-via-fujinet), but the [FujiNet](https://fujinet.online) is a really cool device that sits at the
crossroads of two of my main interests: Atari computers and computer networking.

Thom Cherryhomes is one of the project's leads, and he has some [great videos](https://www.youtube.com/hashtag/fujinet)
about the FujiNet.

I bought one a while back, but haven't done much with it.  Tonight I decided
to spend some time with it, because I wanted to get to know this device better,
and because I have a real-world use for it: I want to [upgrade the firmware](https://atari8.co.uk/firmware/incognito/) in 
my Atari 800's Incognito board.

A while ago, I decided to download and run Thom's [tnfsd Docker container](https://hub.docker.com/r/tschak909/tnfsd-x64)
on my NAS, a Synology DS1618+.  I'm new to Docker, and I'm new to tnfsd, so I wasn't launching it correctly: most importantly
I was using TCP instead of UDP.  I noted that no tnfs client could access the tnfsd on my Synology when it was run in
Docker, but if I ran it manually (e.g., `tnfsd /volume1/docker/tnfsd/data`), clients could connect immediately.

After correcting the settings -- that is: after specifying a directory to mount at /data, and specifying port 16384 -> 16384 (UDP) -- 
any client can connect to my tnfsd running in the container.

One of the cool features I learned about today is that you can mount/unmount disks with your FujiNet while the computer is running,
by using the web interface to mount the disks.  To mount a disk, you use a process similar to what you do in the console config utility: first
you select a server, then you navigate to the file you want:

![1](/images/fujinet/1.png)
![2](/images/fujinet/2.png)
![3](/images/fujinet/3.png)
![4](/images/fujinet/4.png)
![5](/images/fujinet/5.png)

To unmount a mounted disk, click the EJECT link next to the mounted disk in the mount list:

![6](/images/fujinet/6.png)

Tomorrow I will upgrade the firmware on my Incognito.
