#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  trojkat.py
#  
#  Copyright 2018  <>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
def trojkat(a, b, c):
    """
    Funkcja przyjmuje trzy liczby - długości boków trójkąta
    Funkcja sprawdza, czy da się z nich zbudować trójkąt
    Funkcja zwraca True, jeśli się da, False w przeciwnym razie
    """
    wynik = False
    
    if a + b > c and c + a > b and b + c > a:
        wynik = True
        
    return wynik
    
def main(args):
    assert (trojkat(3, 6, 8) == True)
    assert (trojkat(3, 5, 9) == False)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
