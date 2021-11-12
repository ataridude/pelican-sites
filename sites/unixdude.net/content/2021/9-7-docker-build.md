Title: Docker build
Category: Tech
Tags: docker
Date: 2021-9-7
Status: published

I have been having a rough couple months with printers: My Samsung C410w is getting old, so I wanted to
replace it.  My wife recently heard about HP Instant Ink, so she wanted to try that service, but I
decided to buy a monochrome Brother printer -- which was great except my wife decided she needed to be
able to print on cardstock, which the Brother could not do.  So, we returned the Brother and picked up an HP
Envy 6055 -- and proceeded to print more than 750 pages last month.  Suddenly, Instant Ink doesn't look
so affordable.

Anyway, in order to go back to a laser/LED printer, I need to find a replacement to the Envy's scanner.
Well, for 15+ years I have had a CanoScan LiDE 30, which still works fine.  I had been using it for
years with [Mattias Ellert's excellent TWAIN SANE Mac utilities](http://www.ellert.se/twain-sane/),
but Mattias has not maintained this for 4 years now, so I switched to using scanimage on a Raspberry Pi.

Scanimage is fine for me, but there's no WAF there -- and now that I need to increase the WAF of my
scanner setup, and now that I'm learning about
Docker, I wanted to create a Docker image containing a scanner utility that I could run on a Raspberry
Pi connected to the scanner, which could then be left in a convenient location for my wife to use.

In doing some research for
this project, tonight I found [this nice front end](https://github.com/sbs20/scanservjs), which is
also [available as a Docker image](https://hub.docker.com/r/sbs20/scanservjs).  Unfortunately, that
Docker image is only available for amd64 architecture -- but of course my Raspberry Pi is arm64.

I next tried building the image on the raspi, using the Dockerfile in the github source, but even with
an 8GB 4b model, 25+ minutes and it still had a ways to go -- and, it ran out of disk space.

Thankfully, I happen to have a M1 MacBook Air, so I fired up the new M1-specific version of Docker Desktop on that, and built an arm64 image
-- in about 30 seconds!

I quickly [pushed that to Docker Hub](https://hub.docker.com/r/ataridude/scanservjs), then easily ran it 
on my Raspberry Pi with:

    docker container run --device=/dev/bus/usb/001/003 --name scanner -p 8080:8080 --rm ataridude/scanservjs

I'm not done yet, but this is a good place to stop tonight.
