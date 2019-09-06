#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  wejwyj.py
#  


def main(args):
    imie = input("Podaj swoje imie: ")
    nazwisko = input("Podaj swoje nazwisko: ")
    
    print("Witaj", imie, nazwisko,)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
