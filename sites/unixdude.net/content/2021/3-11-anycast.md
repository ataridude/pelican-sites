Title: FRR and Anycast
Slug: frr-and-anycast
Category: Networking
Tags: dns, frr, networking, pi-hole, anycast, raspberry pi
Date: 2021-3-11
Status: published

[FRR](https://frrouting.org) is one of the things I have wanted to configure on my Raspberry Pi, specifically to enable
[anycast](https://en.wikipedia.org/wiki/Anycast) for Pi-Hole.  The reason to do this is that I do not want my Raspberry Pi to be a single
point of failure on the network, especially since it has been connected via wifi, to date anyway.
Once I finish my transition to UniFi, it will be moved to ethernet.

Anycast is useful for services like DNS, DHCP, and MySQL,
and is easier, better in some cases, than using a load balancer.  I wanted to use anycast on my home
network so that I can upgrade or reboot my Raspberry Pi, while ensuring that such maintenance
activity does not negatively affect users on my network.

I started out by creating a DNS entry:

```pihole-anycast.unixdude.net has address 192.168.2.1```

This entry is not strictly required, it's just a convenience.

I then installed FRR on multiple systems -- my Raspberry Pi and a VM
running Ubuntu 20.04.2 LTS, running on my ESXi server.

On each system, I added a loopback address; on the Ubuntu VM I added the following block
to ```/etc/netplan/00-installer-config.yml```:

```
  network:
    ethernets:
      lo:
        renderer: networkd
        match:
          name: lo
        addresses:
          - 192.168.2.1/32
```

On the Raspberry Pi, running Raspbian (stretch), I created a file with the following contents,
saved as ```/etc/network/interfaces.d/lo```.

```
auto lo
iface lo inet loopback

auto lo:0
iface lo:0 inet static
    address 192.168.2.1
    netmask 255.255.255.255
    alias pihole
```

To ensure that this file is loaded, you  might need to confirm that ```/etc/network/interfaces```
includes the following line:

```
source-directory /etc/network/interfaces.d
```

There are two important things to note in the examples above:

- that the address is a /32,
- and that it is added to the loopback interface.

Next, configure FRR to publish that loopback address to the network.  I do this using BGP,
and the relevant part of my configuration is:

    router bgp 65007
     neighbor 192.168.1.254 remote-as 65007
     !
     address-family ipv4 unicast
      redistribute connected route-map anycast
     exit-address-family
    !
    access-list 7 seq 10 permit 192.168.2.1/32
    !
    route-map anycast permit 1
     match ip address 7
    !

As you can see, I am using BGP ASN 65007 on my home network.  My router's IP address is 192.168.1.254,
so I have FRR peer with that address.  Note the route
map and access list configured to publish the loopback's /32 address.

We can take a look at my Ubiquiti USG's BGP routes for that address, and we see the two routes:
```
admin@ubnt:~$ show ip bgp 192.168.2.1/32
BGP routing table entry for 192.168.2.1/32
Paths: (2 available, best #1, table Default-IP-Routing-Table)
  Not advertised to any peer
  Local
    192.168.2.249 (metric 1) from 192.168.2.249 (192.168.2.1)
      Origin incomplete, metric 0, localpref 100, valid, internal, best
      Last update: Sun Mar  7 23:03:51 2021

  Local
    192.168.2.250 (metric 1) from 192.168.2.250 (192.168.2.1)
      Origin incomplete, metric 0, localpref 100, valid, internal
      Last update: Sun Mar  7 13:29:37 2021

admin@ubnt:~$ 
```

And here is its routing table:
```
admin@ubnt:~$ show ip route     
Codes: K - kernel route, C - connected, S - static, R - RIP, O - OSPF,
       I - ISIS, B - BGP, > - selected route, * - FIB route

S>* 0.0.0.0/0 [1/0] via 172.16.0.254, eth0
C>* 192.168.2.0/24 is directly connected, eth1.2
B>* 192.168.2.1/32 [200/0] via 192.168.2.249, eth1.2, 1d17h41m
admin@ubnt:~$ 
```
(some data removed)

Now, anything on my home
network can reach 192.168.2.1/32, and it does not matter which Pi-Hole answers the request, because both
are configured identically.  (I have to manually keep their configurations in sync today, but I am
working on that.)

As I mentioned earlier, a setup like this is useful for DNS, as I am doing here.  It is also useful
for DHCP, where multiple DHCP servers use the same back end, and are all configured with the same
DHCP server identifier.  Using this configuration, the DHCP service stays up as long as at least one
DHCP server is available; the backend database ensures consistency between the pools advertised by
the servers.

Speaking of databases, this solution works similarly with MySQL: one can build a Percona cluster, where
all servers share a single IP address via anycast.  Clients connect to the anycast address, and the
cluster keeps all servers updated to the latest changes.
