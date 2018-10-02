#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  suma_cyfr.py
#  DANE WEJŚCIOWE: liczba "l2" co najmniej dwucyfrowa podawana 
#  przez użytkownika
# DANE WYJŚCIOWE: suma cyfr liczby wydrukowana w terminalu
def sumuj_cyfry(l2):
    suma = 0
    while l2 > 0:
        suma += l2 % 10
        l2 = int(l2/ 10)
        print("Suma cyfr:",suma)
        return suma

def main(args):
    
    # l2 = int(input("Podaj liczbę dwucyfrową:"))
    #
    #while l2 < 10:
        #l2 = int(input("Podaj liczbę dwucyfrową:"))
        assert(sumuj_cyfry(971) == 17)
        assert(sumuj_cyfry(111) == 3)
        assert(sumuj_cyfry(9876) == 30)
        assert(sumuj_cyfry(131) == 5)
        assert(sumuj_cyfry(176) == 14)
        assert(sumuj_cyfry(654) == 15)

    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
