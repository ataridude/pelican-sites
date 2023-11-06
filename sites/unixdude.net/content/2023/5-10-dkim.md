Title: DKIM, Postfix, and FreeBSD
Date: 2023-5-10
Category: Mail
Tags: dkim, postfix, freebsd, icloud
Status: published

Recently, I discovered that I was not able to email my wife's mac.com address from my
mail server here.  [Apple's support document](https://support.apple.com/en-us/HT204137) indicates
that they require DKIM and SPF, and that they support DMARC.  I have long had
[SPF configured](/posts/2019/Feb/14/postfix_relay/), but I had not configured DKIM or DMARC.

Over the weekend, I set up DKIM.  DKIM is basically a public-key cryptographic solution used
to confirm the server that sent an email.  In order to set this up on my FreeBSD 12 server,
I followed [this guide](https://www.prado.it/2012/04/26/how-to-run-postfix-with-opendkim-on-freebsd-9-0/)
which is pretty close to what I ended up doing, and I took some inspiration from
[this guide](https://www.dan.me.uk/blog/2016/06/01/add-dkim-signing-to-freebsd-servers/).
Even with these guides, I had to make a few changes to meet with success on my FreeBSD 12 system.

I chose to install the package, not using source: `pkg install opendkim`

Next, instead of adding the user to the `mail` group, I left off that parameter:

    pw useradd -n opendkim -d /var/db/opendkim -m -s "/usr/sbin/nologin" -w no

I had to do this because I was getting errors while trying to start opendkim.  The errors
complained that the `opendkim` user was a member of the mail group, and that there were
several members of that group.  I'm not sure why that mattered, but I could only get it to work
this way, and I'm good with that.

My milter config file is at `/usr/local/etc/mail/opendkim.conf`, and the contents are what
the other howto shows:

    LogWhy yes
    Syslog yes
    SyslogSuccess yes
    Canonicalization relaxed/simple
    Domain unixdude.net
    Selector iss
    KeyFile /var/db/opendkim/iss.private
    Socket inet:8891@localhost
    ReportAddress root
    SendReports yes

I added the following two lines to `/etc/rc.conf`:

    milteropendkim_enable="YES"
    milteropendkim_uid="opendkim"

I added the following three lines to `/usr/local/etc/postfix/main.cf`:

    smtpd_milters = inet:127.0.0.1:8891
    non_smtpd_milters = $smtpd_milters
    milter_default_action = accept

I generated the key as shown -- `opendkim-genkey -D /var/db/opendkim -d unixdude.net -s iss`.  The
selector (`iss` in this case) can be any string you want.  I went with `iss` because that is
the system name on which this is running.  This places the files in `/var/db/opendkim`, named
`iss.private` and `iss.txt`.

You create two records in DNS; for my server, I created `iss._domainkey.unixdude.net` as a `TXT`
record with the contents of `iss.txt` above:

    [root@iss(F12):/usr/local/etc/mail]host -t txt iss._domainkey.unixdude.net
    iss._domainkey.unixdude.net descriptive text "v=DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDNKaHQWGIuv7uCByXo9/gQon4BAYKXddNS3oS21tXszTz+Z+BN+ROqZSMKyScdqYdn+dP8TBTnWENKV1BCcJLDRLXi8Nmkiafm4MAswxBtPVRwanJVgHAgPqRuy8KARI/I7LmOt4ZxGkngLgfpqC0BXUBDTIOQJNw+GZJctfKuXQIDAQAB"
    [root@iss(F12):/usr/local/etc/mail]

I also created `_adsp._domainkey.unixdude.net` as 
a `TXT` record, with the following contents:

    dkim=unknown

When I test the key, I receive a message saying that the key is not secure, and my google
searches indicate that this means the server is not using DNSSEC.  I'm okay with this.

    [root@iss(F12):/usr/local/etc/mail]opendkim-testkey -vvv -d unixdude.net -s iss -k /var/db/opendkim/iss.private
    opendkim-testkey: key loaded from /var/db/opendkim/iss.private
    opendkim-testkey: checking key 'iss._domainkey.unixdude.net'
    opendkim-testkey: key not secure
    opendkim-testkey: key OK
    [root@iss(F12):/usr/local/etc/mail]

After I checked the key, I started/reloaded the services:

    service milter-opendkim start
    service postfix reload

After that, I was off to the races, and I can now email my wife's mac.con address again.
