Title: Network upgrade
Slug: network_update
Category: Home lab
Tags: synology, r610
Date: 2018-12-28
Status: published

I have a 3-story house, and my office is on the third floor.  Wifi connectivity in the bonus
room over the garage was terrible, so I brainstormed ideas with coworkers and friends about
how to fix this.  As a temporary measure I ran a long ethernet cable from the office to the
bonus room, but this had a very low WAF (wife acceptance factor).

Another idea was to try a wifi extender off of my AT&T fiber Internet router.  This has
higher WAF, but it didn't really seem to help, so I returned it.

A coworker and I came up with a neat idea: I have a conduit running between the 3rd-floor attic
space and the garage.  What about running a long ethernet cable through that conduit, then
moving my router down there?  Great idea, but how do I get the Internet signal to the router?

Another coworker had the solution for that: put a managed switch at both ends of the conduit.
He just happened to have two spare HP ProCurve 1810-24G switches, so I ran an ethernet cable
through the conduit, and voila.

More specifically: I created a VLAN on the switches for the connection between the Fiber/Ethernet
transceiver to the router.  Then I trunked that VLAN over the conduit-cable.  I also trunked my
"Internal" VLAN over the same cable to get it back up to the office.

As a bonus, I got to move my noisy R610 to the garage, making my office much quieter.  Storage
is still in the office, but the server is now remote.  It's nice to have iDRAC, now that my server
is remote to me.

Now I have excellent wifi service on the first floor and bonus room.  So, what about the office
and other parts of the second floor?  I installed my Synology RT1900ac as a wifi access point
in the office; it is now my office switch, and it serves wifi to the parts of the house that
the AT&T router does not reach.
