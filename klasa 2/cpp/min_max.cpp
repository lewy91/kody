/*
 * min_max.cpp
 */


#include <iostream>
using namespace std;

void wypelnij(int tab[], int roz) {
    cout << "Podaj " << roz << " liczb: " << endl;
    for(int i= 0; i < roz; i++){
            cin >> tab[i];
    }
}

void wypelnij_los(int tab[], int roz) {
    srand(time(NULL));
    for(int i= 0; i < roz; i++){
        tab[i]= rand() % 101;
    }
}

void drukuj(int tab[], int roz) {
    for(int i = 0; i < roz; i++){
            cout << tab[i] << " ";
    }
}

int min1(int tab[], int roz) {
    for (int i=0; i < roz; i++) {
        if(tab[i] < min)
            min = tab[i];
        }
        return min
}
int min1(int tab[], int roz) {
    for (int i=0; i < roz; i++) {
        if(tab[i] < min)
            min = tab[i];
        }
        return min
}

int main(int argc, char **argv)
{
	int rozmiar = 5;
    int tab[rozmiar]; // statyczna deklaracja tablicy
    wypelnij_los(tab,rozmiar);
    drukuj(tab,rozmiar);
	return 0;
}

