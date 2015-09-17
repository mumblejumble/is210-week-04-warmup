#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" kittens, litterboxes and catfoods"""


def too_many_kittens(kittens, litterboxes, catfood):
    """ kittens= # of kittens; litterboxes= # of boxes available;
    a catfood boolean."""
    return not (litterboxes >= kittens and catfood)
