#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  potegi.py
#  
def potega_it(a, n):
    wynik = 1
    for i in range(n):
        wynik = wynik * a
    return wynik
def main(args):
    
    a = int(input("Podaj liczbę:"))
    n = int(input("Podaj potęgę:"))
    
    print("{} do potegi {} wynosi {} ". format(a, n, potega_it(a, n,)), end='')
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
