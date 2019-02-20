/*
 * szyfr_przestawieniowy.cpp
 */

#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

#define MAKS 100

void szyfruj(char tb[], int klucz){
    int ile = strlen(tb);
    cout << ile << endl;
    int reszta = ile % klucz; 
    
    if(reszta > 0) {
        for(int i = ile; i < ile + klucz - reszta; i++)
        tekst[i]='.';
    }    
}
    

int main(int argc, char **argv)
{
    char tekst[MAKS];
	int klucz = 0;
    
    cout << "Podaj tekst: " << endl;
    cin.getline(tekst, MAKS);
    cout << cin.gcount();
    cout << strlen(tekst) << endl;
    cout << "Podaj klucz: " << endl;
    cin >> klucz;
    
    szyfruj(tekst, klucz);
	return 0;
}
