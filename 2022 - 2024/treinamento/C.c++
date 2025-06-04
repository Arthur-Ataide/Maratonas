#include <iostream>
#include <vector>

using namespace std;

// void printMatrix(const vector<vector<char>>& matrix) {
//     cout << endl;
//     for (int i = 0; i < matrix.size(); i++) {
//         for (int j = 0; j < matrix[i].size(); j++) {
//             cout << matrix[i][j];
//         }
//         cout << endl;
//     }
// }

void procura(int x, int y, vector<vector<char>>& matrix, int& cont, bool& entra, int* linha, int* coluna) {
    int vetX[] = {1, 1, 0, -1, -1, 0, 1, -1};
    int vetY[] = {0, 1, 1, 1, 0, -1, -1, -1};

    if (matrix[x][y] == '#') {
        if (entra) {
            cont++;
            entra = false;
        }

        matrix[x][y] = cont;

        for (int c = 0; c < 8; c++) {
            int newX = x + vetX[c];
            int newY = y + vetY[c];

            if (newX >= 0 && newX < (*linha) && newY >= 0 && newY < (*coluna)) {
                if (matrix[newX][newY] == '#') {
                    procura(newX, newY, matrix, cont, entra, linha, coluna);
                }
            }
        }
    }
}

int main() {
    int linha, coluna;
    cin >> linha >> coluna;
    vector<vector<char>> matrix(linha, vector<char>(coluna));

    for (int i = 0; i < linha; i++) {
        for (int j = 0; j < coluna; j++) {
            cin >> matrix[i][j];
        }
    }

    int cont = 0;
    bool entra = true;

    for (int i = 0; i < linha; i++) {
        for (int j = 0; j < coluna; j++) {
            entra = true;
            procura(i, j, matrix, cont, entra, &linha, &coluna);
        }
    }

    cout << cont << endl;

    return 0;
}