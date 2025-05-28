#include <bits/stdc++.h>

using namespace std;

int main(){
    
    int y;
    unsigned long long int k; 
    int cont;
    vector<int> d;
    
    cin >> y >> k;
    
    if (k == 1){
        cout << 2 << "\n";
        return 0;
    }

    unsigned long long int x = 1;

    for (int i = 1; i <= sqrt(y); ++i) {
        if (y % i == 0) {
            d.push_back(i);
            if (i != y / i) {
                d.push_back(y / i); 
            }
        }
    }

    sort(d.begin(), d.end());

    
    vector<int> v;
    int ant= 1;
    v.push_back(1);
    
    for (int i:d){
        if (i > 1 && i%ant == 0){
            // cout << i << endl;
            v.push_back(i);
            ant = i;
        }
    }
    if (v.back() != y) 
        v.push_back(y);
    
    int tam = v.size();

    for(int i=0; i < tam; i++) {

        if (i == tam -1){
            // cout << " x = " << x << " k = " << k << " v[i] = " << v[i] << "\n";
            x += (unsigned long long int) v[i] * k;
            break;
        }
        else{
            int a = v[i+1 ] / v[i];
            // cout << "a = " << a  << " y = " << y << " x = " << x << " k = " << k << " v[i] = " << v[i] << " v[i+1] = " << v[i+1] << " Entra no if? "<< (a<k) << "\n";

            if ((a-1) < k){
                k -= (a-1);
                x=v[i+1];
            }

            else{
                x+=(unsigned long long int) v[i]*(k);
                break;
            }

        }
    }
    cout << x << "\n";
    return 0;
}