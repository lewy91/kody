#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  abc.py
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


def main(args):
    
    a = int(input("Podaj pierwsza liczbe: "))
    print(a)
    
    b = int(input("Podaj druga liczbe: "))
    print(b)
    c = int(input("Podaj druga liczbe: "))
    print(b)
    if a > b and a > c:
        print("największe jest", a)
    if b > a and b > c:
        print("największe jest", b)
    if c > a and c > b:
        print("największe jest", c)
    else:
        if c==a==b:
            print("wszystkie liczby są równe")
        else:
            if c==a and c > b:
                print("2 i 3 liczba są najwieksze,mają wartość:",a)
            if c==b and b > a:
                print("2 i 3 liczba są najwieksze, mają wartość:",c)
            if b==a and b > c:
                print("2 i 3 liczba są najwieksze, mają wartość:",b)
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
