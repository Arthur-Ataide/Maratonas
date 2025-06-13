#include <bits/stdc++.h>
using namespace std;

int ultimoDigitoSignificativo(int n) {
    long long resultado = 1;

    for (int i = 2; i <= n; ++i) {
        resultado *= i;

        while (resultado % 10 == 0)
            resultado /= 10;

        resultado %= 1000000000; // apenas os últimos 9 dígitos
    }

    return resultado % 10;
}

int main() {
    int n, instancia = 1;

    while (cin >> n) {
        int digito = ultimoDigitoSignificativo(n);

        cout << "Instancia " << instancia++ << endl;
        cout << digito << endl;
    }

    return 0;
}
