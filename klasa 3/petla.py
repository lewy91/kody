#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petla.py

import random

def main(args):
      
    liczby =[]
    for i in range(5):
        liczby.append(random.randint(1, 30))
    print(liczby)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
