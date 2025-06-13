#include <bits/stdc++.h>
using namespace std;

int main() {
    int n; cin >> n;
    long long a; 
    bool primo;

    while (n--){
        cin >> a;
        primo = true;

        for (long long i=2; i*i <= a; i++) if (a % i == 0) primo = false;
        
        if (primo){
            cout << "Prime" << endl;
        }
        else
            cout << "Not Prime" << endl;
    }
    

    return 0;
}