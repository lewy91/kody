/*
 * potega.cpp
 * 
 * Copyright 2018  <>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */


#include <iostream>
using namespace std;

flat potega_re(float x, int n) {
    if(n== 0) return 1;
    return potega_re(x, n-1) * x;
}

int main(int argc, char **argv)
{
    flat podstawa;
    int wykładnik;
    cout << "Podstawa: "; cin >> podstawa;
    cout << "Wykładnik: "; cin >> wykładnik;
    cout << "Wyniki: "<< potega_re(podstawa, wykładniki);
	
	return 0;
}

