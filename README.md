# Usage & example

SSHator lets you to craft ssh/telnet uris and execute them easily i.e:

   sshator l1s3r:secretpassword@remote.host.com:2323

   telnetator l1s3r:secretpassword@remote.host.com:2323

This will open the default terminal (x-terminal-emulator) with an ssh/telnet
connection to remote.host.com at port 2323 using user l1s3r using
secretpassword.

This is useful if you have a webapp that crafts ssh/telnet links as
`ssh://l1s3r:secretpassword@remote.host.com:2323` or
`telnet://l1s3r:secretpassword@remote.host.com:2323` that you can
associate your webbrowser to sshator.

SSHator implements URI format described by [IETF RFC4248 for telnet](https://tools.ietf.org/html/rfc4248),
there is [darft for SSH](https://tools.ietf.org/html/draft-ietf-secsh-scp-sftp-ssh-uri-04)
but for security purposes do not allow to put the password in clear in the
URI, thats because this software is described as **insecure** ssh/telnet
URI Handler.

# Install and configure

## Prequisites

For ssh URIs you will need to install sshpass (GPL), in debian-like distros:

    apt-get install sshpass

# Install

### Install downloaded package

    python setup.py install


### Install from GitHub

    pip install git+git://github.com/bmiro/sshator.git

### Install from PyPi

    pip install sshator

## Optional configuration

If you want to change the used terminal change your default
`x-terminal-emulator`, in debian-like distros:
    
    update-alternatives --config x-terminal-emulator

# How to register custom URIs in GNU/Linux

[XFCE Custom URI Handler](http://edoceo.com/howto/xfce-custom-uri-handler)

# SECURITY

YES, I know is better to use sshkeys or fingerprints but in *some* *puntal*
*controlled* cases this is very useful.

Is a VERY HIGH! security issue to put passwords in the URI becasue will be
stored in clear! You must use this WITH CARE in very controlled environments.

https://tools.ietf.org/html/draft-ietf-secsh-scp-sftp-ssh-uri-04#section-8

# License

    SSHator is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.



Use with care.
