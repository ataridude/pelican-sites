Title: Bye bye Time Machine
Date: 2024-8-24
Category: General
Tags: macos, backup, rsync
Status: published

In my family, we have a half-dozen Mac laptops -- one for each
of us, and one provided by my employer.  For the personal laptops,
I have been using Time Machine, backing up to my primary Synology
unit.  Unfortunately, Time Machine has proven unreliable, requiring
frequent resets of the backup.  For every system, I have had to
reset the backups multiple times -- that is, I have had to completely
erase the backup on the Synology, and have Time Machine do another
full backup.  This happened to my laptop backup so many times that
a few months back, I migrated my laptop's backup to rsync,
using an NFS automount on my Synology as the destination.  I run
this in a cron job, and I use [healthchecks.io](https://healthchecks.io/)
to watch the status of the cron jobs.

The cron job is simple, just something to run the script every 2 hours:

```
0 */2 * * * root /Users/admin/bin/rsync_mba
```

For the health check, I use a simple check type, with a 1-day period
and a 2-day grace time.  I use the 2-day grace time because I do not
want to get notified of a failed backup just because I unplugged my
laptop for the weekend.

Today, I configured this style of backup for all of my family laptops.
I chose to do it now because my younger son's laptop refuses to restart
Time Machine: it repeatedly warns that the TM hard drive was replaced,
and forces me to confirm that I want to use the drive -- but then it
never starts the backup.  So, his system has been without a backup,
until today when I configured this rsync style backup.

The script itself is also simple, basically just an rsync, but with a
bunch of excludes for things that need to be excluded on macOS.  Also,
the script maintains status files and it has a variable holding the
healthchecks.io ping URL.

The script checks the exit code from rsync, and does various things
based on the exit code.  For example, rsync exit code 23 means the
transfer was partially successful, and I log this as a success, but
I also note that it happened.  rsync exit code 24 means that some
source files disappeared.  I log this as a success without qualification.

---

One thing I maintain is a travel router; this is new in my toolkit, and
I should post about it.  Anyway, a short summary is that my travel
router has an always-on WireGuard VPN to my home network via one of my
Digital Ocean VMs.  I do not want backups to occur while I am connected
this way, so my NAS sets the export to be read/write only for my home 
network's IP subnet.  This way, I do not eat up lots of bandwidth while
I am not at home -- such as when I am using Starlink or wifi at a condo
or resort.
