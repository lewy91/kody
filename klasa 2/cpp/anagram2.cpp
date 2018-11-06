/*
 * anagram2.cpp
*/
#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
	char wyraz[5]="pora";
    int i1, i2, i3, i4;
    for (i1= 0; i1 < 4; i1++){
        for (i2= 0; i2 < 4; i2++){
        if (i1==i2) continue;
        for (i3 = 0; i3 < 4; i3++){
            if (i2 == i3 || i1 == i3) continue;
            i4=1;
            cout << i1 << i2 << i3 << i4 << endl;
            }
        }
    }
	return 0;
}

