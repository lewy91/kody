#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tabliczka_mnozenia.py
#  
def liczby2(a = 10, b = 100):
    for i in range(1, 10):
        for j in range(0,10):
            if i != j:
                print("{}{}".format(i, j), end="")
                ile += 1
        print()
def liczby3(a= 100, b = 1000):
    for liczba in range(1, a+1):
        if liczba %11 !=0:
            print(liczba)
        print()
def main(args):
   
    tabliczka(a, b)
    return 0
    
if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
