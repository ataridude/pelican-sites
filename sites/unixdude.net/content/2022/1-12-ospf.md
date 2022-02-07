Title: Goodbye BGP, hello OSPF
Date: 2022-1-12
Category: Networking
Tags: bgp, anycast, usg, frr, ubiquiti, ospf, raspi, wireguard, zerotier
Status: published

Soon after I learned about [Anycast](https://en.wikipedia.org/wiki/Anycast), I employed it 
on my home network, so that I can have
multiple instances of [Pi-Hole](https://pi-hole.net), mostly so that I can
take down my Raspberry Pi without hearing from the family about how the Internet is down.

Until last night, I was using [BGP](https://www.cloudflare.com/learning/security/glossary/what-is-bgp/) (as part of [FRR](https://frrouting.org)) for Anycast,
[running FRR on my Raspberry Pi](/posts/2021/Mar/11/frr-and-anycast/) and some other devices, and peering those with each other
and with my router.

Well, I got tired of the full mesh that BGP requires, so last night I switched to
OSPF.  It still supports Anycast, but does not require a full mesh of routers, making
it much more suitable to my needs.  I mean, of course I knew BGP was not the right
long-term answer, but it was easy and all of my coworkers were able to help me with any
configuration questions -- and I got to say that I ran BGP at home, which was fun.

---

I have been using [ZeroTier](https://www.zerotier.com) as my VPN solution ever since
[a friend mentioned it](https://mindlesstux.com/2018/09/23/zerotier-multsite-lan-part-1-zerotier-and-making-a-multi-site-lan-man/).
I want to have some redundancy in case ZeroTier goes down, so last night I configured [WireGuard](https://www.wireguard.com) on my Ubiquiti [USG](https://store.ui.com/products/unifi-security-gateway),
as well as one of my offsite systems.  I prefer to run this on my router anyway, since
I don't want my whole network to go down if my Raspberry Pi goes down.  If my network goes down because my router is down,
well, then I have bigger problems than not being able to access my remote systems.

So, I'll use WireGuard as the primary, and ZeroTier as the backup.

---

One of my main goals right now is that I want to retire my Rasperry Pi 3B unit in favor of a
PoE-powered Pi 4B unit, freeing up a power oulet, reducing cables, and generally simplifying
my setup.

---

I'm not done yet, but I'm making good progress on these goals.
