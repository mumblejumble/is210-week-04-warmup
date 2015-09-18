#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" kittens, litterboxes and catfoods"""


def too_many_kittens(kittens, litterboxes, catfood):
    """too many kittens? true means yes, false means no.

    This function finds out whether there're too many cats.

    Args:
        kittens(int): first argument, the number of kittens.
        litterboxes(int): second argument, the number of available litterboxes.
        catfood(mixed): a boolean representing whether or not any catfood
        exists.

    Returns:
        True or False. True means there're too many kittens for litterboxes and
        catfoods. False means there're at lease one litterbox and catfood for
        each kitten.

    Examples:

        >>>too_many_kittens(12, 12, 11)
        False
        >>>too_many_kittens(2, 2, 0)
        True
    """
    return not (litterboxes >= kittens and catfood)
