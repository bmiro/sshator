#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shlex
import subprocess
 
from string import Template

import click

from sshator.uri import extract

@click.command()
@click.option('--term', default='x-terminal-emulator', help='Used terminal')
@click.argument('uri')
def sshator(term, uri):
    """
    " Insecure SSH URI handler, open a SSH connection to given URI in
    " a new terminal.
    """
    extracted_uri = extract(uri)
    username = extracted_uri['username']
    password = extracted_uri['password']
    host = extracted_uri['host']
    port = extracted_uri['port'] 

    cmd_tpl_params = {
        'term': term,
        'username': "%s@" % username if username else '',
        'password': "sshpass -p %s" % password if password else '',
        'host': host,
        'port':  " -p %s" % port if port else ''
    }
    cmd_base =  "${term} -e ${password} ssh ${username}$host ${port}"
    cmd = Template(cmd_base).substitute(cmd_tpl_params)
 
    args = shlex.split(cmd)
    subprocess.call(args)

@click.command()
@click.option('--term', default='x-terminal-emulator', help='Used terminal')
@click.argument('uri')
def telnetator(term, uri):
    """
    " Telnet URI handler, open a Telnet connection to given URI in
    " a new terminal.
    """
    raise NotImplemented
