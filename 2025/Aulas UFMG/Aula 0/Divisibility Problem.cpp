// media

#include <bits/stdc++.h>
using namespace std;

int main() {

    int t, a, b;

    cin >> t;

    for (int i = 0; i < t; i++){
        cin >> a >> b;
        int result = 0;

        if (a % b == 0){
            cout << result << endl;
        }

        else{
            int aux = a / b;
            cout << (aux+1)*b - a << endl;
        }
    }

    return 0;
}