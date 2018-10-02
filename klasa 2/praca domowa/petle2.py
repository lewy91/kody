#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petle-cw2.py
#  
#  


def main(args):
    
    x = int(input("podaj pierwszą liczbe: "))
    y = int(input("podaj drugą liczbe: "))
    
    
    while x >= y:
        y = int(input('Podaj poprawny zakres. Pierwsza liczba musi być mniejsza od drugiej: '))
    
    for z in range(x, y+1):
        print (z, " ", end='')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
