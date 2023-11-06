Title: Mobile Wireguard clients
Date: 2023-7-2
Category: Networking
Tags: wireguard, ipad, iphone, mobile
Status: published

I have been using Wireguard for about a year & a half, when I switched
from ZeroTier to Wireguard for most of my needs.  Unfortunately, since
the start, my Wireguard configuration has been completely manual, and 
very annoying since I had to create a new interface for every client.

No more.

Today I used the [Wireguard Config Generator](https://www.wireguardconfig.com)
to generate the configs (I did not specify my endpoint on the website
of course).  The result was a single server config with keys for two dozen
mobile clients.  Today I configured three of those mobile clients -- one each for
my MacBook Air, my iPhone, and my iPad.

I considered using [Netmaker](https://www.netmaker.io) but decided it was way more than
I needed.  The config generator made that part of the config easy.  Loading the config
into the Mac client was easy.  Loading a config file into the iOS client is not difficult,
but it was way more fun using [qrencode](https://www.cyberciti.biz/faq/how-to-generate-wireguard-qr-code-on-linux-for-mobile/) to generate a QR code to configure the iOS devices.

After I used the Wireguard Config Generator, I updated the client files to specify my endpoint,
then I loaded the configs and was off to the races -- with that part anyway.

I had one more step to make this useful.  The entire point of my Wiregaurd config is to
remotely access my home network. But, since my Wireguard server is on a DigialOcean VM,
and I want my systems to access my home network without masquerading, this required
a configuration change to my FRR config on my DigitalOcean VM.

I just had to add two blocks:

    interface wg0
      ip ospf network non-broadcast
    exit

To the `router ospf` configuration, I added the subnet I dedicated to my Wireguard clients:

    network 192.168.100.128/27 area 0

Now everything can route to my Wireguard clients, and my Wireguard clients can access my
entire network.
