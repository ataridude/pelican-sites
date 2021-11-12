Title: SSH, screen, and tunnels - oh my
Slug: ssh-screen-tunnels-oh-my
Category: Tech
Tags: ssl, shell, unix
Date: 2019-8-28
Status: published

I was recently asked about SSH, tunnels, and reconnecting disconnected sessions. Some people use
[mosh](https://mosh.org/), but I take a different approach, one that does not require any special
server software on the target server.

As with mosh, I recognize that sessions will become disconnected.  As such, I run a
[screen](https://www.gnu.org/software/screen/) session
on a server in the data center, and I initiate all SSH connections from that screen session. I use
screen instead of tmux, mostly because it is extremely simple to create a new screen tab/window from
the command line.  I have created aliases to run a command in a new screen tab.

Here is a sample ~/.screenrc file:

    escape ^Xx
    startup_message off
    vbell off
    backtick 0 10 10 dfh
    backtick 1 10 10 s_uptime
    hardstatus alwayslastline "%{.bG}%H%{-}%{.bW} %-w%{.rW}%f%n %t%{-}%+w %=%{..G}[ %l ]%{..Y} %`"
    defscrollback 5000
    termcapinfo xterm* ti@:te@

In this screenrc file, we note that I run 2 commands every 10 seconds, and that the output of those
commands shows up in my status line.  `dfh` simply prints the output of `df -h` for a certain
filesystem, usually /, in a short format, followed by the current time. `s_uptime` shows load average
for the box.

Early on, I used an alias to create new screen windows/tabs.  I have switched to using a shell script
because I found that when the process terminated (e.g., when the remote server disconnected), the window/tab
disappeared without any explanation as to what happened.  My script catches that and keeps the tab open
until I acknowledge it.

In this script, the variable `$MAIN_SCREENS` holds the hostnames of all systems on which I want to run screen (this
allows this script to function correctly even on systems without screen support), and `$SHORT_HOSTNAME`
is the name of the local system.

Here is the script I use: (the first line is a shebang, but that messes up markdown)

     !/bin/sh
    COMMAND="$*"
    lines=`echo $MAIN_SCREENS | grep -c $SHORT_HOSTNAME`
    if [ $lines -eq 0 ]; then
        # This is not one of the systems running screen, so simply run the command
        ${COMMAND}
    else
        # This system runs screen, so proceed as normal

    FILENAME=`mktemp ~/.screen_tab.XXXXXX`
    cat >${FILENAME} <<EOF
    #!/bin/bash

    function clean_up {
        # Perform program exit housekeeping
        echo "Command exited with exitcode \${EXITCODE}"
        echo
        echo "Press ENTER to continue..."
        echo
        read
        rm -f ${FILENAME}
        exit
    }

    trap clean_up SIGINT

    ${COMMAND}
    EXITCODE=\$?
    if [ \$EXITCODE -gt 0 ]; then
        clean_up
    fi
    rm -f ${FILENAME}
    EOF
    chmod 755 ${FILENAME}
    COMMAND=`echo ${COMMAND} | sed 's/.unixdude.net//'`

    TERMTYPE=""
    if [ ${TERM} = "screen.xterm-256color" ]; then
        TERMTYPE="-T xterm"
    fi
    screen ${TERMTYPE} -t "${COMMAND}" "${FILENAME}"

    fi

Since I always run screen on systems I consider to be jump hosts, I use aliases
to connect to those systems.  Here is an example:

    alias cjb "tabname jump-rdu-01; ssh jump-rdu-01.rdu.domain.com -t 'screen -Rd'; tabname LOCAL_SHELL"

`tabname` is a short script (it could be an alias) that changes the name of the window/tab in my
terminal program: (again, the first line is a shebang)

     !/bin/bash
    printf "\e]1;%s\a" $1

A big trick to all of this is reconnecting after a disconnection.  My solution here is to use a common,
persistent, known value for `${SSH_AUTH_SOCKET}`.  To do that, I modify `SSH_AUTH_SOCKET` variable
on login.  First, I create a symlink called `~/.ssh_auth_socket_${SHORT_HOSTNAME}`
to the actual `$SSH_AUTH_SOCKET`, and then I set `$SSH_AUTH_SOCKET` with a value of
`~/.ssh_auth_socket_${SHORT_HOSTNAME}`.

The value here is that `$SSH_AUTH_SOCKET` never changes between logins, so any existing shell sessions, and any newly
created ones, all reference the same `$SSH_AUTH_SOCKET`, and they always work.

    setenv SHORT_HOSTNAME `hostname`
    find . -maxdepth 1 -name '.ssh_auth_sock*' -mtime +1 -exec rm -f {} \;
    find . -maxdepth 1 -name '.screen_tab*' -mtime +1 -exec rm -f {} \;
    if $?SSH_AUTH_SOCK then
        if ( `echo $SSH_AUTH_SOCK | grep $SHORT_HOSTNAME | wc -l` == 0 ) then
            setenv NEW_SSH_AUTH_SOCK ~${SUDO_USER}/.ssh_auth_sock_${SHORT_HOSTNAME}
            ln -sf ${SSH_AUTH_SOCK} ${NEW_SSH_AUTH_SOCK}
            setenv SSH_AUTH_SOCK $NEW_SSH_AUTH_SOCK
        endif
    endif

This is tcsh code, but bash can do the same thing of course.
