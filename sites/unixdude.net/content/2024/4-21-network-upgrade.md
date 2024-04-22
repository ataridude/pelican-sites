Title: Home network upgrade
Date: 2024-4-21
Category: Network
Tags: ubiquiti, udm-se, usg, ospf, wireguard
Status: published

Over the weekend, I upgraded my network:  I replaced my Ubiquiti USG with a
UDM-SE.  I debated between the UDMP and UDM-SE, and decided on the UDM-SE
because of its added features.  As part of this upgrade, I retired my
self-hosted UniFi Controller in favor of the one on the UDM-SE.

I have never done a UniFi network upgrade before, so I really wasn't sure what
to expect.  It was actually surprisingly easy, but my custom setup required a
slightly modified process and configuration after the upgrade.

My biggest questions were: How does one actually replace a UniFi router?  How
does one replace the router and controller with a single unit, as I was doing?
I did some research but was never truly clear about the answers to these
questions.

Replacing a controller seems to be a pretty well-known process: Take a backup,
then forget all devices in the old controller, and import the backup into the
new controller.  My concern was that I was also replacing the router, and I did
not know what the controller in the UDM-SE would do with the USG in the backup.
It did exactly what I wanted it to do: It detected the USG in the backup, and
it replaced the USG with itself.

I thought I was going to have to adopt the UDM-SE and somehow figure out how to
replace the USG with it, because I thought I would need to configure the UDM-SE
with an IP address to add it to the network, then replace that address with the
one in the USG, but I was completely wrong.

I had to use a slightly different process because of the configuration I had on
the USG: I used a ```config.gateway.json``` file to configure WireGuard and
OSFP, and I had to remove that before taking my backup.  After the migration, I
had to add my WireGuard links and configure OSPF on the UDM-SE.

In the end, this worked great except for one thing: The web UI does not seem to
allow me to configure OSPF on the WireGuard links.  OSPF on the UDM-SE peered with
my local routers, but not with my remote ones, so my routes were not optimal.
There are multiple ways to get to my remote sites, so the routes were there,
they just added another hop or 2.  This kind of defeats the purpose of WireGuard
for me.

I did a lot of searches, and found [this 7-month-old post](https://community.ui.com/questions/FRR-questions-on-UDM-Pro-SE-3-1-x/b6d128c2-5b32-49a1-b0cf-e6441e781575),
and wondered if it would still work in the current version of the OS.  Turns out
it works great: After starting the FRR service, I was able to use ```vtysh``` to
add the WireGuard links to my OSPF area, and to add the neighbors.  It required
one more thing to work.  I had to configure the interfaces with ```ip ospf network
non-broadcast```:

```
interface wgclt1
 ip ospf cost 1
 ip ospf dead-interval 40
 ip ospf network non-broadcast
exit
```

These entries mirror the other ones created on the UDM-SE, and the ```ip ospf
network non-broadcast``` mirrors what I had on the USG.

After I did all that, OSPF peered to the routers at the remote sites, and the
correct entries were in the routing table.  The config persists across reboots,
and it works perfectly.
