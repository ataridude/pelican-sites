Title: MinFS
Category: Tech
Date: 2021-10-28
Status: published

Over the last month, I have been continuing my work at automating my systems and have made a lot of
progress in that effort.

Part of that will be relocating some files that I still want web-accessible, but not on this website.
Enter [DigitalOcean Spaces](https://www.digitalocean.com/products/spaces/), and [MinFS](https://github.com/minio/minfs) to access it.

Set was super simple: After installation, I edited `/etc/minfs/config.json` to set my Spaces
access key and secret key, then added the /etc/fstab entry, created the directory, and mounted it.

`/etc/fstab`:
```
https://nyc3.digitaloceanspaces.com/unixdude /mnt/unixdude minfs defaults,cache=/tmp/unixdude-minfs 0 0
```

```
[root@ansible-test(U20):67:/mnt/unixdude/ataridude]df -h .
Filesystem      Size  Used Avail Use% Mounted on
MinFS            64T     0   64T   0% /mnt/unixdude
[root@ansible-test(U20):68:/mnt/unixdude/ataridude]ls -l
total 0
-rw-rw---- 0 root root 67748394 Oct 27 22:57 atari-5200-jumpy-video.mov
[root@ansible-test(U20):69:/mnt/unixdude/ataridude]
```

The URL for that file is: [https://unixdude.nyc3.digitaloceanspaces.com/ataridude/atari-5200-jumpy-video.mov](https://unixdude.nyc3.digitaloceanspaces.com/ataridude/atari-5200-jumpy-video.mov)

Pretty slick.  I'll be adding more to that space over time.

Also: 64T - wow!
