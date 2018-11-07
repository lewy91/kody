/*
 * palindrom.cpp
 */


#include <iostream>

using namespace std;

int zlicz(char tb[]) {
    int i = 0;
     while(tb[i] != '\0') i++;
     return i;
 }
 
bool palindrom(char w[], int rozmiar){
    bool czyPal = true;
    int polowa = rozmiar / 2;
    int j = 0;
    for(int i = rozmiar - 1; i > polowa ; i = i - 1) {
      if (w[i] == w[j]){
          j++;
          }   
      else{
        czyPal = false;
        break;  
        }   
    }  
    return czyPal;
}

int main(int argc, char **argv)
{   const int roz = 50;
    char tekst[roz];
    cout << ("Wprowadź wyraz: ");
    cin.getline(tekst, roz);
	if (palindrom(tekst, zlicz(tekst)) == 1){
            cout << "jest";
    }
    else{
        cout << "nie jezd";
        }
	return 0;
}
