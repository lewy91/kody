#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  liczby.py
#  
#  

def main(args):
    a = int(input("Podaj pierwsza liczbe: "))
    b = int(input("Podaj druga liczbe: "))
    c = int(input("Podaj  trzecia liczbe: "))
    x = 0
    print(a,b,c)
    
    if a>b and a>c:
        x=a
    elif b>a and b>c:
        x=b
    elif c>a and c>b:
        x=c
    
    print ("Najwieksza liczba to: ", x)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
