Title: ZeroTier Is Fun
Slug: zerotier-is-fun
Category: Tech
Tags: networking
Date: 2021-5-18
Status: published

I recently installed a [Synology DS118](https://www.synology.com/en-us/products/DS118) at a friend's house
for remote backup using [Synology's Hyper Backup solution](https://www.synology.com/en-us/dsm/feature/hyper_backup).
The DS118 is on my ZeroTier "storage" network, a network shared by the main Synology at my house -- that way,
my main NAS backs up to a local system (that is, something on the same layer 2 network), which makes that part
easy.  I was able to prime the backup at my house and ensure that everything worked, then I gave the DS118 to my
friend to take to his house -- and the backup worked exactly as it did when both units were at my house.
This is why I like ZeroTier.

Today I realized that the DS118 is not sending notification emails, and I definitely want it to be able to send email
when it has something to report.  I enabled notifications on the DS118 and configured it to send me mail.  It seems
my friend's ISP is blocking outbound email, because every test message failed -- that is, until I reconfigured
the DS118 to relay through the raspberry pi at my house, which is on the same ZeroTier "storage" network.

The raspberry pi is my home mail relay, through which all other systems at my house send mail to my DigitalOcean droplet:
the raspi and the droplet are on the same ZeroTier network.

So, now I have notifications from my DS118, relayed through the raspi at my house, using two ZeroTier networks.

ZeroTier is fun.
