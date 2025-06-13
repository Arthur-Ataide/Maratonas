#include <bits/stdc++.h>
using namespace std;

int main(){
    int n; cin >> n;
    int a, b, x, y;

    while (n--){
        x++;
        y++;
        cin >> a >> b >> x >> y;


        int maiorB = max(b*(a-x), b*(x-1));
        int maiorA = max(a*(b-y), a*(y-1));
        cout << max(maiorA, maiorB) << endl;
    }
    
}