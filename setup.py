# -*- coding: utf-8 -*-

from setuptools import setup                                                                         
 
INSTALL_REQUIRES = [
    'click'
]
 
setup(
    name='sshator',
    version='0.0.3',
    packages=['sshator'],
    url=u"",
    license='GPLv3',
    install_requires=INSTALL_REQUIRES,
    entry_points="""
        [console_scripts]
        sshator=sshator.cli:sshator
        telnetator=sshator.cli:telnetator
    """,
    author=u"Bartomeu Miro Mateu",
    author_email=u"bartomeumiro at gmail dot com",
    description=u"Insecure SSH/Telnet URI handler"
)

