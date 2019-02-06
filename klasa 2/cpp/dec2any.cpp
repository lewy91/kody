/*
 * dec2any.cpp
 */


#include <iostream>
#include <cmath>
using namespace std;

int cyfry[]={0,1,2,3,4,5,6,7,8,9,65,66,67,68,69,70};

int dec2any(int liczba, int podstawa, int tab[]){
    int i = 0;
    do {
       tab[i] = liczba % podstawa;
       liczba = liczba / podstawa;
       i++; 
    }
    while ( liczba != 0);
    return i-1;
}
void any2dec(int tab[]){
    int podstawa= 0;
    do{ 
        cout << "Podstawa[2;9]:";
        cin >> podstawa;
    } while (podstawa < 2 || podstawa > 9);
    
    cout << "Podaj liczbę";
    cin.getline(liczba, 0);
    int ile= 0;
    cout <<"Ile cyfr? ";
    cin >> ile;
    for(int i = 0; i < ile; i++)
        do{
            cout << "Podaj cyfrę[0-" << podstawa-1 << "];";
            cin >> tab[i];
        } while (tab[i] < 0 || tab[i] > podstawa);
    //konwersja begin
    int liczba10 = 0;
    for (int i=0; i<ile; i++){
        liczba10 += tab[i] * pow(podstawa, ile-i-1);
    }
    cout << "Wynik: " << liczba10;
}
void bin2dec(int tab[]){
        ;
}
int main(int argc, char **argv)
{   
    int tab[10];
    int liczba, podstawa;
    cout << "Podaj liczbę i podstawę systemu docelowego: ";
    cin >> liczba >> podstawa;
    int i = dec2any(liczba, podstawa, tab);
    cout << "Wynik: ";
    while (i > -1){  
        if (podstawa > 10 && tab[i] > 10)
            cout << (char)cyfry[tab[i]];
        else
             cout << tab[i];
        i--;
    }
    cout << endl;
    any2dec(tab);
    return 0;
}

