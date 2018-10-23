/*
 * NWD_euklides.cpp
 */


#include <iostream>
using namespace std;

int nwd_klasyczny(int a, int b)
{
    int licznik = 0;
    while (a != b)
    {
        if (a > b)
            a= a - bl
        else
        b = b - a;
        licznik++;
    }
int nwd_opt(int a,int b) {
while (a > 0) {
    a = a % b;
    b = b - a;
    licznik++;
    };
    cout << "Powtórzeń: " << licznik << andl;
    return b;
}

int main(int argc, char **argv)
{
	int a,b:
    cout << "Podaj a: ";
    cin >> a;
    cout << "Podaj b: ";
    cin >> b;
    cout << "NWD(" << a << " i " << b << ") =";
	return 0;
}

