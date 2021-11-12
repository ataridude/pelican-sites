Title: testssl.sh
Slug: testssl_sh
Category: Tech
Tags: ssl, shell, unix
Date: 2018-7-2
Status: published

Last week, I needed to make some changes to my employer's production website, but
before I made those changes in production, I wanted to test them. Unfortunately
for me, our dev server is unreachable by Qualys, so I had to come up with another
way to test those changes.

Enter [testssl.sh](http://www.testssl.sh/).  testssl.sh is a shell script that
can be used to do testing very simliar to what Qualys does, from a Unix system.

To get started, clone the testssl.sh repo:

`git clone https://github.com/drwetter/testssl.sh.git`

I was able to make and test the changes I needed on our dev system, before going
to production.  I was able to confirm that my changes were correct, in a non-production environment.

Many thanks to Dirk Wetter for this excellent tool.

Check it out.
