Title: healthchecks.io
Category: Tech
Tags: monitoring
Date: 2021-11-15
Status: published

Recently, [a friend](http://mindlesstux.com) introduced me to [healthchecks.io](https://healthchecks.io), a service for monitoring cron jobs.  
A week or so ago, I configured several of my cron jobs to be monitored through this system, and it has already helped me:
yesterday I received a notification that an rsync job did not run, and the reason for that failure turned out to be
a filesystem that was unintentionally unmounted.  I remounted the filesystem, and today I received a notification that
the rsync job finished as expected.  What a great service.
