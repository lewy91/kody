/*
 * petla.cpp
 */


#include <iostream>

#include <cstdlib>
using namespace std;

void wypelnij_los(int tab[], int roz) {
    srand(time(NULL));
    for(int i = 0; i < roz; i++) {
        tab[i] = rand() % 30;
    }
}
void drukuj(int tab[], int roz) {
    for(int i = 0; i < roz; i++) {
        cout << tab[i] << " ";
    }
}

int main(int argc, char **argv)
{
	int roz = 5;
    int tab[roz];  
    wypelnij_los(tab, roz);
    drukuj(tab, roz);
	return 0;
}
s
