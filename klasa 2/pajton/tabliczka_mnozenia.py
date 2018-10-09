#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tabliczka_mnozenia.py
#  
def tabliczka(a, b):
    for i in range(1, a+1):
        for j in range(1,b + 1):
            print("{:>3} ".format(i * j), end= ' ')
        print()
def main(args):
    a=int(input("Podaj zakres 1: "))
    b=int(input("Podaj zakres 1: "))
    tabliczka(a, b)
    return 0
if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
