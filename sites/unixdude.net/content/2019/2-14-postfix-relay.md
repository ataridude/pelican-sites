Title: Postfix relay configuration
Slug: postfix_relay
Category: Mail
Tags: postfix, spf, email
Date: 2019-2-14
Status: published

Like most people in my industry, I use multiple email addresses at multiple providers.
Used to be, I could configure all of my email addresses in my mail client and just send
through my mail server and -- voila -- my email would go out as whatever address I
wanted to use.

Then along came Sender Policy Framework (SPF).  SPF is a great email-related technology
that is designed to protect the integrity of sending domains.  Unfortunately for me, 
adoption of SPF meant that I could no longer send mail through my mail server using one
of my other email addresses.  Specifically, I could no longer send mail through my
server as my gmail.com or mac.com addresses.  I couldn't complain, because my server is
an origination point for gmail.com or mac.com.

Fortunately, there's a fix for this: [Postfix's "sender_dependent_relayhost_maps" feature](http://www.postfix.org/postconf.5.html#sender_dependent_relayhost_maps "Postfix's sender_dependent_relayhost_maps feature").

The idea: configure all of my devices to send mail through my mail server, and to have
the mail server itself relay as necessary depending on sending address.  My goal: send
mail directly if it originates from my domain; relay gmail mail through smtp.gmail.com,
and relay iCloud mail through smtp.mail.me.com.

To use that, I defined a few settings in my postfix main.cf file:

```
smtp_sender_dependent_authentication = yes
sender_dependent_relayhost_maps = hash:/usr/local/etc/postfix/sender_relay
smtp_sasl_auth_enable = yes
smtp_sasl_password_maps = hash:/usr/local/etc/postfix/sasl_passwd
smtp_tls_note_starttls_offer = yes
smtp_tls_policy_maps = hash:/usr/local/etc/postfix/tls_policy
smtp_tls_security_level = encrypt
smtp_use_tls = yes
smtp_enforce_tls = yes
smtp_sasl_security_options = noanonymous
smtp_sasl_mechanism_filter = plain
smtp_sasl_tls_security_options = noanonymous
```

For my server, smtp_sender_dependent_authentication is not strictly necessary, because
I am the only one sending through my mail server.  I include it here because it is
needed for a more general solution.

The real magic occurs as a result of sender_dependent_relayhost_maps.  This setting
configures the different relays based on sending address.  My sender_relay file looks like this:

```
address@gmail.com      [smtp.gmail.com]
address@mac.com        [smtp.mail.me.com]:submission
```

The smtp_sasl_password_maps configuration is also needed because both
Gmail and iCloud require authentication before an email can be relayed through their
servers.  To do this, I have configured application-specific passwords in both systems,
and the sasl_passwd file looks like this:

```
address@gmail.com               address@gmail.com:PASSWORD
address@mac.com                 address@mac.com:PASSWORD
```

The TLS policy maps are required because the relays require encryption; the tls_policy file's
contents are:
```
[smtp.gmail.com]:587 encrypt
[smtp.mail.me.com]:587 encrypt
```

Of course, you must run postmap on each of these files prior to using them.

On FreeBSD, which is my OS of choice, things were slightly more complicated than they
otherwise might have been.  I was not able to use the default postfix package, because it is
not compiled with Cyrus SASL client support.  A quick `make configure` in
`/usr/ports/mail/postfix` allowed me to enable Cyrus SASL client support.  After a
`make` and `make install` I was ready to test. Many thanks to [Brad](https://blog.bradlab.tech/) for
helping me test.

Now I can eliminate all of the extra accounts on all of my devices.
