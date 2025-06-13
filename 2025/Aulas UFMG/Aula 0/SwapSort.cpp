#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, a;
    cin >> n;
    vector<pair<int, int>> vet;
    vector<pair<int, int>> result;

    for (int i = 0; i < n; i++){
        cin >> a;
        vet.push_back({a, i});
    }

    sort(vet.begin(), vet.end());

    for (int i = 0; i < n; i++){
        pair<int, int> aux;
        if (vet[i].second != i){
            for (int j = i+1; j<n; j++){
                if (vet[j].second == i)
                    vet[j].second = vet[i].second;
            }
            result.push_back({vet[i].second, i});
            vet[i].second = i;
        }
    }

    int tam = result.size();
    cout << tam << endl;

    for (int i = 0; i < tam; i++){
        cout << result[i].first << " " << result[i].second << endl;
    }
}
