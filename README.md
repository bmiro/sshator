
= Install and configure =

You will need to install sshpass, in debian-like distros:

    `apt-get install sshpass`

If you want to change the used terminal change your default x-terminal-emulator,
in debian-like distros:
    
    `update-alternatives –config x-terminal-emulator`

= Usage & example =

sshator lets you to craft ssh uris and execute them easily i.e:

   sshator l1s3r:secretpassword@remote.host.com:2323

This will open the default terminal (x-terminal-emulator) with an ssh
connection to remote.host.com at port 2323 using user l1s3r using
secretpassword.

This is useful if you have a webapp that craft ssh links as
ssh://l1s3r:secretpassword@remote.host.com:2323 and you
associate your webbrowser to sshator.

YES, I know is better to use sshkeys but in *some* *puntal* *controlled* cases
this is very useful.


Use with care.
