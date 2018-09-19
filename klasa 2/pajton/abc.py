#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  abc.py
#  
#  Copyright 2018  <>

#def max(a, b, c):
    #a = int(input("Podaj pierwsza liczbe: "))
    #b = int(input("Podaj druga liczbe: "))
    #print(b)
    #c = int(input("Podaj druga liczbe: "))
    #print(b)
    #if c==a==b:
    #    print("wszystkie liczby są równe i mają wartość",a)
    #else:
    #if c==a and c > b:
    #        print("1 i 3 liczba są najwieksze,mają wartość:",a)
    #    if c==b and b > a:
    #        print("2 i 3 liczba są najwieksze, mają wartość:",c)
    #    if b==a and b > c:
    #        print("1 i 2 liczba są najwieksze, mają wartość:",b)
    #else:
    #        if a > b and a > c:
    #            print("największe jest", a)
    #        if b > a and b > c:
    #            print("największe jest", b)
    #        if c > a and c > b:
    #            print("największe jest", c)
    def maks(a,b,c):
        maks = a
        if b > maks:
            maks = b
        if c > maks:
            maks = c
        return maks
    def main(args):
        assert(maks2(3,2,1) == 3)
        assert(maks2(2,3,1) == 3)
        assert(maks2(1,2,3) == 3)
        assert(maks2(1,1,3) == 3)
        assert(maks2(3,1,1) == 3)
        assert(maks2(1,3,1) == 3)
        assert(maks2(1,3,3) == 3)
        assert(maks2(3,3,1) == 3)
        assert(maks2(3,3,3) == 3)

    
            
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
