#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """wink and nudge times default

    variable wink and nudges would print twice if numwink was not being over
    written by another interger.

    Args:
        wink(mixed): first argument.
        numwink(str, optional): a string with default: 2, could be overwritten.

    Returns:
        A statement that states "Know what I mean? assigned first argument times
        second argument number, if not over written: 2.

    Examples:
        >>> know_what_i_mean('happy', 3)
        'Know what I mean? happyhappyhappy, nudge nudge nudge'

        >>> know_what_i_mean('one', 2)
        'Know what I mean? oneone, nudge nudge'

    Raises:
        Error: An error occurred accessing the know_what_i_mean object.
    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
