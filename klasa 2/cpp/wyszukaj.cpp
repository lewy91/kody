/*
 * wyszukaj.cpp
 */

#include <iostream>
using namespace std;

void wypelnij_los(int tab[], int roz)
{
    srand(time(NULL));  
    for(int i = 0; i < roz; i++)
    {
        tab[i] = rand() % 101;
    }
}

void drukuj(int tab[], int roz)
{
    for(int i = 0; i < roz; i++)
    {
        cout << tab[i] << " ";
    }
}

void sort_insert(int tab[], int n)
{
    cout << "\nSortowanie przez wstawianie" << endl;
    int i, j, tmp;
    int licznik = 0;
    for(i = 1; i < n; i++)
    {
        tmp = tab[i];
        j = i - 1;
        while(j >= 0 && tab[j] >tmp)
        {
            tab[j+1] = tab[j];
            j--;
            licznik ++;
        }
        tab[j+1] = tmp;
    }
    cout << "Liczba porównań: " << licznik << endl;
}

int szukaj_bin_rek(int p, int k, int tab[], int szuk){
    if (p <= k) {
        int s = (p + k) / 2;
        if (tab[s] == szuk) return s;
        if (szuk < tab[s]) 
            return szukaj_bin_rek(p, s-1, tab, szuk);
        else 
            return szukaj_bin_rek(s + 1, k, tab, szuk);
    }
    return -1;
}

int szukaj_bin_it(int tab[], int n, int szuk){
    int p, k, s;
    p = 0; 
    k = n - 1;
    while (p <= k){
        s = (p + k) / 2;
        if (tab[s] == szuk) 
        return s;
        else if (szuk < tab[s]) k = s - 1;
        else p = s + 1;
    }
    return -1;
}

int main(int argc, char **argv)
{
	int n = 20;
    int tab[n];
    wypelnij_los(tab, n);
    drukuj(tab, n);
    int szuk = 0;
    cout << "Podaj liczbę: ";
    cin >> szuk;
    sort_insert(tab, n);
    drukuj(tab, n);
    
    //int indeks = szukaj_bin_it(tab, n, szuk);
    int indeks = szukaj_bin_rek(0, n-1, tab, szuk);
    
    if (indeks >= 0)
        cout << "\nZnaleziono na indeksie " << indeks << endl;
    else
        cout << "\nNie znaleziono "<< endl;
        
	return 0;
}
