#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    num = {1: 'one', 2: 'two', 3: 'tree'}
    num_rev = dict(map(reversed, num.items()))
    print(num_rev)