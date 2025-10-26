Title: Comics
Date: 2025-10-26
Category: General
Tags: docker
Status: published

For 15-20 years, I have run a script that gathers daily images for several comic strips.
Recently, this script stopped working, and rather than fix it (it is Perl code that at
this point has become unmaintainable) I decided to look for an OSS solution.

Web searches quickly led me to [dosage](https://dosage.rocks).

Dosage can output HTML files, and it seems that, generally, people have Dosage output
saved to a directory accessible on a web server.  I wanted to do this too, but I also
wanted to have this fully deployed via Ansible, and I wanted it to integrate with my
Traefik server, with everything running in Docker images.

Also, there is [an issue](https://github.com/webcomics/dosage/issues/346) affecting Dosage's
ability to download from GoComics, but there is also a workaround (posted in that thread)
that is not yet available in the main Dosage code, so I wanted my Docker container to
incorporate that fix.

I ended up with a very simple Docker container, a volume to store the images, and a cron job
to run load the strips each day.

Credit for the download.sh script goes to Simon Szustkowski, in his [dosage-docker](https://github.com/simonszu/dosage-docker)
repository.

I tried out Simon's image, but found that it was not suitable for my needs, due to the GoComics
issue mentioned above.  And, my solution is not a fork of his, but rather a similar solution.

The code to build my Dosage docker image is found [here](https://github.com/ataridude/dosage-docker).

I'm using this as a one-shot container -- I do not leave it running.

-----

The other side of this is having it on the web.  Since I am already running Traefik, and
since I only need to present a few files on the web, I decided to add this as another
web server container connected to Traefik.  Among other benefits, this means I easily get SSL
using my existing configuration.

All I had to do on this side was to add another DNS entry (comics.unixdude.net), another
call to my [traefik-website](https://github.com/ataridude/ansible/tree/master/roles/traefik-website)
role, and a little bit of configuration of that new role.

-----

The only remaining pieces were to add a directory in which to store the images, and a cron job
to run the dosage-docker container once daily.
