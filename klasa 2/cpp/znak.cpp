/*
 * znak.cpp
 * 
 */


#include <iostream>

using namespace std;

void licz_znaki(char tab[]){
    int i = 0;
    int biale = 0;
    while(tab[i] != '\0') {
    cout << tab[i] << " "; 
    if (tab[i] == ' ' || tab[i] == '\t')
        biale++;
    else 
        cout << tab[i];
    i++;
    }
    cout << "\nZnaków białych: " << biale << endl;
}

int main(int argc, char **argv)
{
    const int rozmiar= 50;
    char znaki[rozmiar];
    cout << " Jak sie nazywasz? ";
    cin.getline(znaki, rozmiar);
    cout << "Cześć " << znaki << endl;
    licz_znaki(znaki);
	return 0;
}

