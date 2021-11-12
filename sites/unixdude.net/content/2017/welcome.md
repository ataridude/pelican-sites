Title: Welcome
Date: 10/26/2017 10:21
Category: General
Status: published

A while ago, a friend suggested that I should start a blog.  Around that
same time, a coworker introduced me to DigitalOcean.  I quickly set up a
VM at DigitalOcean (that VM is serving this web page), and installed
FreeBSD 11.

I looked at WordPress and other popular blogging tools, but all were
overkill for what I want to do, and all would overtax the small VM I am
running.  I finally settled on Pelican, after a coworker showed me [his blog](http://blog.bradlab.tech/){:target="_blank"}.

I played around with all of the Pelican themes, and wanted one that
would look good on all screen sizes, so it had to be a
[Bootstrap](http://www.getbootstrap.com){:target="_blank"} derivative.

I use a second FreeBSD system for the development version of this blog.
That system is a VM running on my ESXi server.  I develop and deploy
there, then I deploy the production version here via rsync.

I won't get into the details of everything this VM does,
but it functions as a:

- Mail server, running Postfix + Dovecot + SpamAssassin + Sieve + Roundcube
- Web server, running Apache serving a dozen or so virtual hosts, all of which use [Let's Encrypt certificates](https://www.letsencrypt.org/){:target="_blank"}
