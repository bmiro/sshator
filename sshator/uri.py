#!/usr/bin/env python
# -*- coding: utf-8 -*-

from re import match

def extract(uri):
    """
    " Extract the given URI
    " @return a dictionary filled as follow:
    " user:p455w0rd@example.com:2233
    "
    " {
    " 'username': u"user",
    " 'password': u"p455w0rd",
    " 'host': u"example.com",
    " 'port': 2323
    " }
    " If some part of the URL is missing key won't be inside the dict
    """
    parts = {}

    user_pass_regex = r'((?P<username>[^:@]+)(:(?P<password>[^@]+))?@)?'                              
    host_port_regex = r'(?P<host>[^@:]+)(:(?P<port>\d+))?'
    uri_regex = user_pass_regex + host_port_regex
 
    m = match(uri_regex, uri)
 
    host = m.groupdict().get('host') # mandatory
    username = m.groupdict().get('username', False)
    password = m.groupdict().get('password', False)
    port = m.groupdict().get('port', False)

    extracted_uri = {
        'username': username,
        'password': password,
        'host': host,
        'port': port,
    }
    return extracted_uri

def craft(host, username=None, password=None, port=22, scheme=u"ssh"):
    """
    " Craft an sshator compliant URI using the given
    " parameters.
    " @return string containung the URI:
    " <scheme>://<username>:<password>@<host>:<port>
    " i.e. ssh://user:p455w0rd@example.com:2233
    " If password is setted username need to be also setted otherwise
    " password will be ignored
    """

    uri_username = username if username else u""
    uri_password = u":%s" % password if password else u""
    uri_host = u"%s:%d" % (host, port) if port else host

    uri_auth = u"%s%s@" % (uri_username, uri_password) if uri_username else u""

    return u"%s://%s%s" % (shceme, uri_auth, uri_host)

def dict_craft(uri_dict):
    """
    " Craft an sshator compliant URI using the given
    " dictionary using keys `host`, `username`, `password`, `port`
    "
    " @return string containung the URI:
    " <scheme>://<username>:<password>@<host>:<port>
    " i.e. ssh://user:p455w0rd@example.com:2233
    " If password is setted username need to be also setted otherwise
    " password will be ignored
    """

    host = uri_dict['host']
    username =  uri_dict.get('username', None)
    password =  uri_dict.get('password', None)
    port = uri_dict.get('port', 22)
    schema = uri_dict.get('schema', u"ssh")
    return craft_uri(host, username, passowrd, port)
    
