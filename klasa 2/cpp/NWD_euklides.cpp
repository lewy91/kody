/*
 * NWD_euklides.cpp
 */


#include <iostream>
using namespace std;

int nwd_klasyczny(int a, int b)
/*
 * nwd_euklides.cpp
 */


#include <iostream>
using namespace std;
 
 int nwd (int a, int b) {
     int licznik = 0;
     while (a > 0){
         a = a % b;
         b = b - a;
         licznik++;
         
    };
     cout << "Powtórzeń: " << licznik << endl;  
     return b;
}
 
int nwd_klas(int a, int b) {
    int licznik = 0;
    while (a != b)
    {   
        if (a > b)
            a = a - b;
        else
            b = b - a;
        licznik++;
    }
    cout << "Powtórzeń klasyczny: " << licznik << endl;
    
    return 0;
}

int main(int argc, char **argv){
    int a, b;
        cout << "Podaj a: ";
        cin >> a;
        cout << "Podaj b: ";
        cin >> b;
        cout << nwd(a, b);
        cout << nwd_klas(a, b);
    
    return 0;
}
