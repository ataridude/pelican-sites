Title: Better spam blocking
Date: 2022-9-15 9:30
Category: Mail
Tags: postfix
Status: published

As mentioned previously, I continue to be inundated with spam email.  Fortunately,
every spam has an observable email format: the email comes in the form of user@word1.word2.TLD.

This allows me to update my `blocked_senders` file to defer every email in that format with a 450, using
this pattern:

    /@.*\..*\..*$/ 450 No such address

When I first started doing this, I was manually watching inbound email logs to see what was deferred.  I
would then update the `blocked_senders` file to add the domain as a 521 (for obvious spam), or with an
"OK" for obviously valid email or unknown spam.  Then I rebuild the `blocked_senders` map and reload postfix.

After a while, I noticed that the domain (word2.TLD) is always a parked domain.  I wrote a script to
check each domain found in the deferred email logs to detect whether the domain is parked.  With this
information, the script makes the decision and updates postfix for me: Parked domains are added to
`blocked_senders` with a 521, and other domains are added with an "OK" to allow my server to receive
the mail.

This is basically a simple knock-to-enter form of blocking, and so far it is working very well.

So now I get emails like this, as my scripts do their work:

    Adding spam domain: [mydealmenia.com]
    Adding valid domain: [mail.goodreads.com]
    Adding valid domain: [readaloudrevival.com]

All totally automatic now.

The code I used can be found [here](https://github.com/ataridude/block_spam).
