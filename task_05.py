#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" true or false"""


def defaults(my_required, my_optional=True):
    """True or False.

    compares if they are identical.

    Args:
        my_required(bool): random string.
        my_optional(bool): random string with default True.

    Returns:
        whether booleans assigned to arguments are identical.

    Examples:

        >>>defaults(True)
        True

        >>>defaults(True, False)
        False

        >>>defaults(True, True)
        True
    """
    return my_optional is my_required
