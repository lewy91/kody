#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   rysowanie_prostokąta.py
#   DANE WEJSCIOWE: boki a i b prostokąta
#   DANE WYJŚCIOWE:prostoką narysowany w terminalu gwiazdkami o rozmiarach podanych przez użytkownika
#   EXTRA: znak, którym rysowany jest prostokąt, pobierz od użytkownika

def main(args):
    
    a= int(input("podaj długość boku a:"))
    
    b= int(input("podaj długość boku b:"))
    
    znak= input("Podaj znak:")
    
    for i in range(a):
        for j in range(b):
            if j > i and j < b:
                print(" ", end='')
            else:
                print(znak, end='')
        print()
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
