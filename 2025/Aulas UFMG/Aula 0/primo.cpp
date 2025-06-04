// facil

#include <bits/stdc++.h>
using namespace std;

int main() {
    long long n; cin >> n;
    if (n <= 1){
        cout << "nao" << endl; return 0;}

    else{
        for (int i = 2; i*i <= n;i++)
            if (n % i == 0){
                cout << "nao" << endl;
                return 0;
            }
    }
    
    cout << "sim" << endl;
    


    return 0;
}