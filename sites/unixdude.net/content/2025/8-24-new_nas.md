Title: New NAS
Date: 2025-8-24
Category: General
Tags: hardware, synology, frr, backup
Status: published

I recently discovered that my offsite backup NAS, a Synology DS118 with a 12TB drive in it,
had filled up.  I considered several solutions to this problem, eventually deciding to replace
the DS118 with a DS225+.  Since [Synology now requires Synology-branded drives](https://www.tomshardware.com/pc-components/nas/synology-requires-self-branded-drives-for-some-consumer-nas-systems-drops-full-functionality-and-support-for-third-party-hdds),
I had to either buy two new drives or I had to shift some drives around.

To save some money, I decided to shift drives around rather than buy two new drives for the DS225+,
because the 12TB drive would work nicely in my local backup NAS, and I recently purchased two 6TB
Synology HDDs to replace dead drives in my local NAS units.  I decided to buy a single 16TB
Synology drive in conjuntion with using one of my recently purchased 6TB drives; as a result, I
have about 22TB in the DS225+.

I decided to configure these drives as two basic volumes, rather than as a single volume, because I
don't care about redundancy for this unit, and because I do not want a single failed drive to
destroy all of my remote backup data, which is what would happen in a JBOD setup.

After I installed the 16TB drive, I started priming the backup.  For my remote backup solution,
I use Synology's Hyper Backup because it works well, works fine over WireGuard, and is easy to use.
A short while after starting to prime the new backup, I noticed that the operation was taking
forever... I traced this down to a bad switch port on my desktop switch: The backup was running
at only 100Mbps!  Simply relocating the cable fixed the issue.

Once the backup is primed, I will take it back to my friend's house, and I will reconfigure Hyper
Backup to point to the new location.

Access to the unit will be over WireGuard -- the DS225+ will connect to one of my DigitalOcean VMs, and
OSPF will allow me to easily route to it.  For WireGuard on the Synology, I used
[this guide](https://www.youtube.com/watch?v=uPjAirU4occ) to find the installation SPK, then
I followed the standard WireGuard setup.  I generated the key by running something like this: `wg genkey | tee private.key | wg pubkey > public.key`.

Then I configured the WireGuard client on the DS225+ by creating `/etc/wireguard/wg0.conf` with these contents:

    [Interface]
    Address = 192.168.x.x/30
    SaveConfig = false
    Table = off
    PrivateKey = GENERATED_PRIVATE_KEY

    [Peer]
    PublicKey = PEER_PUBLIC_KEY
    AllowedIPs = 0.0.0.0/0, ::/0
    Endpoint = hostname:port
    PersistentKeepalive = 3

Once the peer was configured as well, a simple `wg-quick up wg0` on the DS225+ was all I needed to establish
the connection.

In order to ensure that this connection is started when the NAS boots, I also ran `wg-autostart enable wg0`
on the DS225+.

WireGuard + FRR really is a great solution for remote systems like this offsite backup NAS.
