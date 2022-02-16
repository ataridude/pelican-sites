Title: Cable cleanup
Date: 2022-2-11
Category: Lab
Tags: update, cables, rack, routing, ospf, wireguard, usg, ubiquiti, digitalocean
Status: published

A quick update on my OSPF cutover.  With one exception, everything has worked great.
The one exception is that OSPF would not work over the WireGuard link between my USG
and my primary DigitalOcean VM that runs FreeBSD 12 and FRR7.  I thought that was odd,
since OSPF worked fine over WireGuard between the USG and another VM at DigitalOcean,
running Ubuntu 20.04 LTS and FRR8.

After many web searches, I found [this page](https://docs.netgate.com/pfsense/en/latest/vpn/wireguard/routing.html)
that mentions the two requirements to getting OSPF working over WireGuard:

* The WireGuard interface must be set to Non-Broadcast network type
* OSPF neighbors must be statically configured

Once I did that on both the USG and the FreeBSD/FRR7 system, my two routers neighbored
correctly, and my FreeBSD/FRR7 VM obtained the entire LSDB.

---

Two weeks ago I finished racking everything in my new rack, and last weekend I
cleaned up the cables behind and below the rack.

As you can see from these "before" pics, the cables were a mess.  There was
way too much slack, and just a jumble of cables below the rack.

![before-1](/images/lab/before-1.jpg)
![before-2](/images/lab/before-2.jpg)
![before-3](/images/lab/before-3.jpg)

This jumble has been there for at least a year, and I finally bundled the cables and
moved the slack to the other side of the wall.  I think the result is pretty awesome.

![after-under-1](/images/lab/after-under-1.jpg)
![after-under-2](/images/lab/after-under-2.jpg)

The finished lab looks pretty good:

![rack](/images/lab/rack.jpg)

For those who are interested, here's what's in and around that rack:

* U12: TRENDnet 24-port Keystone patch panel, with VCE inline couplers and VCE blanks
* U11: Ubiquiti USW-Lite-16-PoE and Ubiquiti USG
* U10: Cisco 2611 (Lab R1)
* U9: Cisco 2610 (Lab R2)
* U8: Cisco 2610 (Lab R3)
* U7: Cisco 2960 (Lab S1)
* U6: Cisco 2960 (Lab S2)
* U5: Cisco 3750 (Lab S3)
* U3-U4: Shelf holding Raspberry Pi 4B (8GB) and Lenovo M900 Tiny
* U2: Empty
* U1: Pyle PDU

I left U2 empty so that I can reach the latches that allow my Networx rack to swing out.
There is no shelf at U11; the UI devices are simply resting atop the Cisco in U10.

Below the rack are my Synology DS220+, a Grandstream DP750, a Linksys PAP2, and my UPS.
