Title: Dealing with spam
Date: 2022-8-1
Category: Mail
Tags: postfix
Status: published

Somehow I have been added to several mailing lists, all run by the same organization.  The emails look legit, and
are ones that I might have subscribed to, but I cannot get off of them no matter what I do -- it seems that they
ignore all requests to be removed from the list.  Postfix to the rescue: Postfix has a `smtpd_sender_restrictions`
setting, which allows the user to deny specific senders -- but the caveat is that it uses the envelope sender,
not the "from" header in the message.

I took note of the envelope senders, and have added those to a `blocked_senders` file:

    /6045-.*-2315@.*redacted.com/ 521 No such address

My `smtpd_sender_restrictions` configuration includes the line `check_sender_access pcre:/usr/local/etc/postfix/blocked_senders,`
which includes the single line above.  Earlier versions of my blocked_senders file had multiple
rows for this one sender, but I finally realized that the first and last numbers (6045 & 2315) are
the account number, and that the middle number was an ever-increasing campaign ID.

Now, when mail comes in from those addresses, it is rejected, and I don't ever see it. And, for some
reason, this particular sender keeps sending me a half-dozen emails a day, despite getting 521 errors
for every email.

-----

More than this, though, I have noticed that spammers have gotten much more sophisticated: they register
real domains and run their spam servers on static IP addresses with real A & PTR DNS records, so they
look legitimate and they pass most of Postfix's spam tests.  I mark every such email as spam, and I add
the envelope sending domain to the same blocked senders file mentioned above.  Every day this
blocked_sender config catches multiple attempts from these same spammers. Until they register more real
hostnames and domain names, I might be good on spam blocking again!
