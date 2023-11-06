Title: Using the program map type in autofs
Date: 2022-9-15 9:50
Category: Tech
Tags: autofs, nfs
Status: published

I recently learned about the `program` map type in the Linux automounter.

You can read about it [here](https://man.cx/auto.master#heading3), but there is little information about it,
and I was unable to find any web pages about it, so I am writing this post since it might help others.

The NFS automounter on Linux can take a static map, which we all know, including wildcard.  The static map
is in the format of `key options export_location`.

Well, the automounter also supports a `program` map type.  The `program` map type specifics a program to run,
and the program returns the export location for any key in that mount location:

    /mnt/nfs program:/usr/local/sbin/mapper.py

It's really quite simple: The program takes the `key` as argument 1, and returns the `export_location` that
would be found in a static map.  The program does not return anything else -- it returns only the location of
the NFS export.  If the program returns anything else, autofs reports an error in the logs.  The documentation
does say that it can return "everything but the key," but this was not my experience.

In my example, if the user executes `cd /mnt/nfs/blah`, the automounter executes `/usr/local/sbin/mapper.py blah`,
and the script might return something like `filer.example.com:/volume1/maps/abc/123`, which would then be mounted
at `/mnt/nfs/blah` as expected.

This can be useful if you want a fully dynamic automount map that is maintained by a group other than the sysadmins
of a server.  In my case, a development organization maintains a list of exports in a file that the script retrieves
with HTTP.  The script then parses that list of exports in the program, and any given key returns the correct location for the
automounter to mount.  The developers can now update their own autofs maps without involving the admins.
