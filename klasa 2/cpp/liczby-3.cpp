/*
 * liczby-23.cpp
 */


#include <iostream>
using namespace std;


int liczby3() {
    int ile = 0; // deklaracja + inicjacja = definicja
    for (int i = 1; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            for (int k = 0; k < 10; k++) {
            if (i !=j && i!=k && j!=k){ //instrukcja warunkowa (warunek) &&= and
                cout << i << j << k << " "; // wydrukuj i, j, k i zrób spację między nimi
                ile++;
            }
        }
        cout << endl;
    }
}
    return ile;
}

int main(int argc, char **argv)
{
	cout << "\n\nLiczb 3-cyfrowych: " << liczby3() << endl;
	return 0;
}

