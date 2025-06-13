#include <bits/stdc++.h>
using namespace std;

int main() {
    int n; cin >> n;
    int cont = 1;
    while (n){

        cout << "Teste " << cont << endl;
        int rst = 1;

        for (int i = 0; i < n; i++){
            int aux; cin >> aux;
            if (rst == aux){
                cout << rst << endl;
            }
            rst ++;
        }
        cin >> n;
        cont ++;
    }
    
    return 0;
}