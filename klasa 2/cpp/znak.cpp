/*
 * znak.cpp
 * 
 */


#include <iostream>

using namespace std;

void licz_znak(char tab[]){
    int i = 0;
    int biale, inter, licz;
    biale = inter = licz = 0;
    while(tab[i] != '\0') {
    cout << tab[i] << " "; 
    //if (tab[i] == ' ' || tab[i] == '\t')
    //    biale++;
    //else 
    //    cout << tab[i];
    switch (tab[i]) {
        case' ': biale++; break;
        case'\t': biale++; break;
        case',': inter++; break;
        case'.': inter++; break;
        default: licz++; break;
        }
    i++;
    }
    cout << "\nZnaków białych: " << biale << endl;
    cout << "\nInterpunkcyjne: " << inter << endl;
    cout << "\nReszta: " << licz << endl;
}

void ascii(char tab[]){
    int i=0;
    while(tab[i] != '\0') {
        cout << (int)tab[i] << " ";
        i++;
    }
}
void zamiana_liter1(char tab[]){
    int i=0;
    int z=0;
    while(tab[i] != '\0'){
        z= (int)tab[i];
        
        if (z >= 65 || z<=90)
             z += 32;
        else if (z >= 97 || z <=122)
             z -= 32;
        cout << (char)z;
        i++;
    }
}


int main(int argc, char **argv)
{
    const int rozmiar= 50;
    char znak[rozmiar];
    cout << " Jak sie nazywasz? ";
    cin.getline(znak, rozmiar);
    cout << "Cześć " << znak << endl;
    //licz_znaki(znaki);
    ascii(znak);
    zamiana_liter1(znak);
    
	return 0;
}

