#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Lewandowski_przeszukiwanie.py
#  
#  Copyright 2018  <>
import random
def wypelnij(szuk):
    for i in range(10):
        szuk.append(random.randint(0, 50))
    print(szuk)
    
def main(args):
    szuk = []
    wypelnij(szuk)
    i = int(input("Podaj liczbę: "))
    for j in range (len(szuk)):
        if szuk.count(i) == 0 or i > 51:
            print("Element nieznaleziony")
            i += 1
            return
        else:
            print("Element znaleziony")
            return
            
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
