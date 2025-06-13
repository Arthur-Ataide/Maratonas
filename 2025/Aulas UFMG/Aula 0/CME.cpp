#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, x; cin >> n;

    while (n--){
        cin >> x;
        if (x % 2 == 0){
            if (x == 2) cout << 2 << endl;
            else cout << 0 << endl;
        }

        else cout << 1 << endl;

    }
    


}

