#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


def getpath(subp='.'):
    path = os.path.abspath(__file__)
    path = os.path.split(path)[0]
    path = os.path.join(path, subp)
    return os.path.abspath(path)
