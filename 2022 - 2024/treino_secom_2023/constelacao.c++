#include <iostream>
using namespace std;

int main(){
    int vectorX[100];
    int vectorY[100];
    int n;

    cin >> n; 


    for (int i = 0; i < n; i++)
        cin >> vectorX[0] >> vectorY[0];
    

    for(int i = 0; i < n; i++)
        for(int j = i; j < n; j++)
            for (int k = j; k < n; k++)

}