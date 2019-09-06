/*
 * wejwyj.cpp
 */


#include <iostream>
using namespace std;
int main(int argc, char **argv)
{
    const int rozmiar = 30; // deklaracja stałej
    char znaki[rozmiar]; // deklaracja tablicy znakowej 
	cout << "Jak się nazywasz? ";
    cin.getline(znaki, rozmiar);
    cout << "Witaj wędrowcze " << znaki << endl;
	return 0;
}

