#!/usr/bin/env python

import sys, os, re
import shlex
import subprocess

from string import Template

if __name__=='__main__':

    ssh_uri = sys.argv[1]

    user_pass_regex = r'((?P<username>[^:@]+)(:(?P<password>[^@]+))?@)?'
    host_port_regex = r'(?P<host>[^@:]+)(:(?P<port>\d+))?'
    uri_regex = user_pass_regex + host_port_regex

    match = re.match(uri_regex, ssh_uri)

    username = match.groupdict().get('username', False)
    password = match.groupdict().get('password', False)
    host = match.groupdict().get('host') # mandatory
    port = match.groupdict().get('port', False)

    cmd_tpl_params = {
        'term': 'x-terminal-emulator',
        'username': "%s@" % username if username else '',
        'password': "-p %s" % password if password else '',
        'host': host,
        'port':  " -p %s" % port if port else ''
    }
    cmd_base =  "${term} -e sshpass ${password} ssh ${username}$host ${port}"
    cmd = Template(cmd_base).substitute(cmd_tpl_params)

    args = shlex.split(cmd)
    subprocess.call(args)

