# -*- coding: utf-8 -*-

from setuptools import setup                                                                         
 
INSTALL_REQUIRES = [
    'click'
]
 
setup(
    name='sshator',
    version='0.0.1',
    packages=['sshator'],
    url='https://ba.rtom.eu/sshator',
    license='GPLv3',
    install_requires=INSTALL_REQUIRES,
    entry_points="""
        [console_scripts]
        sshator=sshator.cli:sshator
        telnetator=sshator.cli:telnetator
    """,
    author=u"Bartomeu Miró Mateu",
    author_email='b@rtom.eu',
    description='Insecure SSH/Telnet URI handler'
)

