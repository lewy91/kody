#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petle-cw1.py
#  
#  Copyright 2018  <>
#  

def main(args):
    a = 0
    b = 0
    while a < 75:
         a = int(input("Podaj  liczbę:"))
         c = b + a
    print("Za duża liczba", c)
      
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
