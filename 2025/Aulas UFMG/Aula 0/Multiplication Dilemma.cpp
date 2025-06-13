
#include <bits/stdc++.h>
using namespace std;

int potenciaDe10(int expoente) {
    int resultado = 1;
    for (int i = 0; i < expoente; i++) {
        resultado *= 10;
    }
    return resultado;
}

int main() {
    int n;
    cin >> n;
    int x, y;

    for (int i = 0; i < n; i++) {
        cin >> x >> y;
        char negA = '+', negB = '+';

        if (x < 0) {
            negA = '-';
            x *= -1;
        }
        if (y < 0) {
            negB = '-';
            y *= -1;
        }

        string a = to_string(x);
        string b = to_string(y);

        int lenA = a.size() - 1;
        int lenB = b.size() - 1;

        for (int j = 0; j < lenA + 1; j++) {
            if (a[j] != '0') {
                for (int c = 0; c < lenB + 1; c++) {
                    if (b[c] != '0') {
                        if ((negA != '-' and negB != '-') or (negA == '-' and negB == '-')) {
                            if ((lenB - c + 1 or lenA - j + 1) and not(j == 0 and c == 0)) cout << " + ";
                            cout << (a[j] - '0') * potenciaDe10(lenA - j) << " x ";
                            cout << (b[c] - '0') * potenciaDe10(lenB - c);
                        } else {
                            if (j == 0 and c == 0) cout << "-";
                            else if (lenB - c + 1 or lenA - j + 1) cout << " - ";

                            cout << (a[j] - '0') * potenciaDe10(lenA - j) << " x ";
                            cout << (b[c] - '0') * potenciaDe10(lenB - c);
                        }
                    }
                }
            }
        }
        cout << "\n";
    }
}