/*
 * liczby.cpp
 */


#include <iostream>
using namespace std;
int main(int argc, char **argv)
{
    int a, b, c;
    a = b = c= 0;
    cout << "Podaj pierwsza liczbe: "<< endl;
    cin >> a;
    cout << "Podaj druga liczbe: "<< endl;
    cin >> b;
    cout << "Podaj trzecia liczbe: "<< endl;
    cin >> c;
    
    if (a>b and a>c) cout << "Najwieksza liczba to: "<< a <<endl;
    if (b>a and b>c) cout << "Najwieksza liczba to: "<< b <<endl;
    else cout << "Najwieksza liczba to: "<< c <<endl;
    
	
	return 0;
}

