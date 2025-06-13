#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m; 
    cin >> n >> m;
    vector <int> vetI(n, 0);
    vector <int> vetJ(m, 0);

    for (int i =0; i < n; i++){
        for (int j = 0; j < m; j++){
            int val; cin >> val;
            vetI[i]+= val;
            vetJ[j] += val;
        }
    }


    int maior = 0;

    for (int i =0; i < n; i++){
        maior = max(maior, vetI[i]);
        // cout << vetI[i] << " linha " << i << endl;
        for (int j =0; j < m; j++){
            maior = max(maior, vetJ[j]);
            // cout << vetJ[j] << " coluna " << j << endl;
        }
    }

    cout << maior << endl;

    return 0;
}
