Title: Lab, and network upgrade
Slug: catalyst
Category: Tech
Tags: network
Date: 2021-3-12
Status: published

I like networking -- always have.  However, today, my networking knowledge is only okay -- but I want it to be great!  My goal is to
achieve CCNP certification in 6 months.  To help with this effort, I have added a Cisco lab to my home network.
It is old equipment (2x 2610, 1x 2611, 3x 2950) running IOS 11 and 12, but that's okay, and it will soon be
upgraded: as I cut over to Ubiquiti equipment for my home network, the 2960s I am using today will move to the lab,
and I will add a layer 3 switch as well.  The lab routers will also be upgraded to something running IOS 15, but I'm not sure what yet.

I like network diagrams, so for fun, here is a diagram of my current home network:

![Home network 2021](/images/home_network_2021-03.jpg)

And here is my Cisco lab:

![Cisco lab 2021-03](/images/cisco_lab_2021-03.jpg)

As you can probably imagine, I have been fun expanding my use of VLANs and BGP in my home network.

I have further plans as well:

- Introduce a MySQL cluster.  This will use an anycast address (see earlier post on anycast) so that clients
can specify the anycast address and not care which server they talk to.
- Introduce a router between my lab and my home network.  Current plan is to use Cumulus VX for this, because
I want to learn Cumulus Linux as well.
- I want the lab completely separated from my home network; as you can see from the diagrams above, the lab
is connected to my home network.  This will change as I introduce Cumulus VX to the mix.

Planned network upgrades:

- The 2960 in the middle will be replaced with a [Ubiquiti USW-Lite-16-PoE](https://store.ui.com/collections/unifi-network-routing-switching/products/usw-lite-16-poe)
- The MikroTik hap AC in the entertainment center will be replaced with a [USW-Flex-Mini](https://store.ui.com/collections/unifi-network-routing-switching/products/usw-flex-mini) and a [U6-LR-US](https://store.ui.com/collections/unifi-network-access-points/products/unifi-6-long-range-access-point)
- The HP ProCurve at my desk will be replaced with a [US-8](https://store.ui.com/collections/unifi-network-routing-switching/products/unifi-switch-8-150w)

At that point, all of the switches and APs will be PoE, meaning I will have only a single place for battery
backup of the entire network, and fewer wall warts.
