/*
 * sortowanie.cpp
 * 
 */


#include <iostream>
using namespace std;

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
void zamien1(int &a, int &b){
    int tmp = a; //zmienna pomocnicza
    a = b;
    b = tmp;
}
void zamien2(int tab[], int i){
    int tmp;
    tmp = tab[i];
    tab[i] = tab[i] + 1;
    tab[i + 1] = tmp;
}
void sort_bubble(int tab[], int n){
    cout <<"\nSortowanie bąbelkowe \n";
    for (int j = n - 1; j > 0; j--){
        for(int i = 0; i < j; i++){
            if (tab[i]>tab[i+1])
                zamien1(tab[i],tab[i+1]);
        }   
    }
}

int main(int argc, char **argv)
{
    int roz = 20;
    int tab[roz]; // statyczna deklaracja tablicy
    //wypelnij_los(tab,rozmiar);
    //drukuj(tab,rozmiar);
    wypelnij_los(tab, roz);
    drukuj(tab, roz);
    int a = 10;
    int b = 20;
    zamien1(a, b);
    zamien2(tab, roz);
    sort_bubble(tab, roz);
    drukuj(tab, roz);
    return 0;
}

