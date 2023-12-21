Title: macOS Mail issue with postfix
Slug: macos-mail-postfix
Category: Mail
Tags: email, postfix, macos
Date: 2019-5-14
Status: published

I recently got a new MacBook Pro, and as I was setting up the mail configuration on that laptop,
I found that I was unable to send mail through my mail server.  I use Apple Mail, and usually
it works great for me, but in this case it was not working with my Postfix server.

I made several attempts at fixing this issue, but I always got the same error:

    postfix/submission/smtpd[70940]: NOQUEUE: reject: RCPT from REDACTED[X.X.X.X]: 554 5.7.1 <recipient@anywhere.com>: Recipient address rejected: Access denied; from=<sender@example.com> to=<recipient@anywhere.com> proto=ESMTP helo=<[REDACTED]>

After exhausting everything I could think of, and after much troubleshooting, I determined
that all settings were correct: other systems could send mail through my Postfix server,
but I still had the problem with the new laptop.

At one point I had the idea to disable Apple Mail's SMTP server checkbox that sets the
application to "Automatically manage connection settings," so I did that and I confirmed the
settings that it had been automatically managing -- the port and TLS/SSL setting (587/SSL)
and authentication configuration.

Once I disabled the automatic option, everything worked correctly.  I didn't actually change any
configuration, and all of the settings were correct, it just doesn't work automatically.

I post this that others might find it useful, and that I might find it when I set up my
next system.
