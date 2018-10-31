/*
 * anagram.cpp
 */


#include <iostream>
using namespace std;

int zlicz(char tab[]){
    int i = 0;
    while(tab[i] != '\0') i++;
    return i;
}

void wyswietl(char tekst[], int roz) {
    for(int i = 0; i < roz; i++){
        cout << tekst[i];
    }
}
void anagram(char tab[], int roz){
    for
}

int main(int argc, char **argv)
{
	const int roz= 50;
    char tekst[roz];
    cin.getline(tekst, roz);
    wyswietl(tekst, zlicz(tekst));
    return 0;
}

