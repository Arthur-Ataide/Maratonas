#include <bits/stdc++.h>
using namespace std;

int main(){
    int n; cin >> n;

    while (n--){
        int x; cin >> x;
        vector<int> vet;
        int tam = x;

        while (x--){
            int a; cin >> a;
            vet.push_back(a);
        }

        int menor = vet.back();
        vet.pop_back();
        tam --;
        int cont = 0;

        while (tam--){
            int atual = vet.back();
            vet.pop_back();
            if (menor < atual){
                cont++;
            }
            else menor = atual;
        }
        cout << cont << endl;

    }
    

}
