Title: Sharing Unix shell config between systems
Category: Unix
Tags: shell, git
Date: 2017-11-11
Status: published

Like most people who work on Unix, I have shell accounts on hundreds of systems.  Very few
of these systems share a home directory (e.g., via NFS), so I need another way to maintain
a common shell configuration between systems.

Based on the design of a former coworker, I have built such a system using git, symlinks, and
scripts.

I use four git repos for my Unix account configuration:

* a "bin" directory for home
* a "bin" directory for work
* a "bin" directory for everywhere
* an environment directory

All of those directories are private git repos, stored on Bitbucket.  I will
eventually host my own git repo, but for now I use Atlassian's excellent
service.

Of the four repos listed above, the "home" bin directory exists only on personal systems,
the "work" directory exists only on employer systems, and the "everywhere" directory is
shared on all systems.

The environment directory includes such things as:

* tcsh config
* bash config (for systems on which tcsh is not available)
* ssh config
* screenrc
* vimrc
* a script to configure my environment on a new host

I use three additional scripts in conjunction with the repos:

* one to inform me when a sync is required
* one to perform the git sync
* one to copy an existing config to a new host (such as one that does not have git installed)

Obviously I can run "git push" and "git pull" manually, but since there are four
repos here, it was easier to script it.

My "update_repos.sh" script looks like this:

```sh
#!/bin/sh

echo "Update my_env"
cd ~/.my_env
git pull
git push

if [ -d ~/bina ]; then
    echo
    echo "Update bina"
    cd ~/bina
    git pull
    git push
fi

if [ -d ~/binh ]; then
    echo
    echo "Update binh"
    cd ~/binh
    git pull
    git push
fi

if [ -d ~/binw ]; then
    echo
    echo "Update binw"
    cd ~/binw
    git pull
    git push
fi
```

I use symlinks from main files, into my environment directory:
```sh
.bash_profile@ -> .my_env/tcsh/bash_profile
.bashrc@ -> .my_env/tcsh/bashrc
.cshrc@ -> .my_env/tcsh/cshrc
.login@ -> .my_env/tcsh/login
.logout@ -> .my_env/tcsh/logout
.ssh@ -> .my_env/ssh
.vimrc@ -> .my_env/vimrc
```

To bootstrap a host, I check out the applicable repos on the host, then run my setup script, which looks like this:
```sh
#!/bin/sh
ln -sf .my_env/tcsh/bashrc     ~/.bashrc
ln -sf .my_env/tcsh/cshrc      ~/.cshrc
ln -sf .my_env/tcsh/login      ~/.login
ln -sf .my_env/tcsh/logout     ~/.logout
ln -sf .my_env/vimrc           ~/.vimrc
ln -sf .my_env/screenrc        ~/.screenrc
rm ~/.ssh
ln -s  .my_env/ssh             ~/.ssh
if [ -e '/auto/downloads/Set up new host/ssh_config/id_rsa' ]; then
    cp '/auto/downloads/Set up new host/ssh_config/id_rsa' ~/.ssh
fi
```

Two comments about this script:

1. ~/.ssh is not removed if it is a directory.  This does complicate matters on systems that already have a ~/.ssh
directory.  In those cases I blow away ~/.ssh and rebuild it as a link.
2. /auto is where my NFS automounter lives.  /auto/downloads is on my NAS and in keeping with best-practices
my private key only exists on appropriate systems.

Comment below if you have any questions or comments about this setup.
