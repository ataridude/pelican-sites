Title: I love SSH tunnels
Slug: ssh_tunnels
Category: Networking
Tags: unix, shell, ssh
Date: 2018-3-15
Status: published

Everyone who knows me well knows that tunnels in SSH represent one of my all-time-favorite features, ever.  Why?  Simple: They
are so immensely useful.

Say you are debugging an issue on server, as I am today, and you need a mail server running on that server.  But, that server is a
production system, and you cannot install a mail server on it.  Want a quick "mail server"?  Use an SSH tunnel:

`sudo ssh -L 25:mail.domain.com:25 daniel@localhost`

This will ssh back to localhost as user daniel, but will set up a listener on port 25 that points to mail.domain.com, port 25.

Voila... a temporary "mail server" on your system, torn down when you no longer need it.

You can also use tunnels for many other things.  I also use SSH to tunnel VNC, RDP, Synergy, Video Station from my Synology -- and I even use it to access my ESXi console.

SSH tunnels are easy to implement in an SSH config file:
```
host demo
hostname demo.example.com
user daniel
ForwardAgent yes
LocalForward 5022 192.168.0.2:22
LocalForward 5947 192.168.0.47:5900
LocalForward 24800 192.168.0.2:24800
```
