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

int fibonacci_re(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    return fibonacci_re(n-1) + fibonacci_re(n-2);
}

int main(int argc, char **argv)
{
    int n;
    cout << "Podaj numer wyrazu ciągu "; cin >> n; 
    for (int i=0; i <= n; i++){
        if (i < 2) continue;
        else{
            cout << (float)fibonacci_it(i) / (float)fibonacci_it(i-1)<< endl;
        }
    }
	return 0;
}

