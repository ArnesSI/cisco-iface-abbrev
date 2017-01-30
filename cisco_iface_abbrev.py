# -*- coding: utf-8 -*-
########################################################################
#
# MIT License
#
# Copyright (c) 2017 Matej Vadnjal <matej@arnes.si>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
########################################################################

"""
Module to abbreviate and/or lengthen Cisco IOS interface names.
"""

__author__ = 'matej'
__version__ = '1.0.0'


SHORT_LONG = {
    'Fa': 'FastEthernet',
    'Gi': 'GigabitEthernet',
    'Te': 'TenGigabitEthernet',
    'Fo': 'FortyGigabitEthernet',
    'Et': 'Ethernet',
    'Eth': 'Ethernet',
    'Vl': 'Vlan',
    'FD': 'Fddi',
    'PortCh': 'Port-channel',
    'Po': 'Port-channel',

    'Tu': 'Tunnel',
    'Lo': 'Loopback',
    'Vi': 'Virtual-Access',
    'Vt': 'Virtual-Template',
    'EO' : 'EOBC',
    'Di' : 'Dialer',

    'Se': 'Serial',
    'PO': 'POS',
    'PosCh': 'Pos-channel',
    'Mu': 'Multilink',
    'AT': 'ATM',

    'Async': 'Async',
    'Group-Async': 'Group-Async',
    'MFR': 'MFR',
}
LONG_SHORT = {}
for s, l in SHORT_LONG.items():
    LONG_SHORT[l] = s
# These have multiple short versions, select the more common one to shorten to.
LONG_SHORT['Port-channel'] = 'Po'
LONG_SHORT['Ethernet'] = 'Et'


def get_both(in_name):
    """
    Expands or shortens Cisco interface name given in in_name.
    Returns a tuple of short and long version.
    """
    for l, s in LONG_SHORT.items():
        if in_name.startswith(l):
            return (in_name, in_name.replace(l, s))
    for s, l in SHORT_LONG.items():
        if in_name.startswith(s):
            return (in_name, in_name.replace(s, l))
    return (in_name,)


def get_short(in_name):
    """
    Returns the abbreviated name.
    """
    for l, s in LONG_SHORT.items():
        if in_name.startswith(l):
            return in_name.replace(l, s)
    return in_name


def get_long(in_name):
    """
    Returns the expanded name.
    """
    for s, l in SHORT_LONG.items():
        if in_name.startswith(s):
            return in_name.replace(s, l)
    return in_name
