#include <iostream>
#include <vector>

using namespace std;

int linha, coluna;
vector<vector<char>> matrix;

// Define os 8 movimentos possíveis (em relação a uma célula)
int movimentos[8][2] = {
    {1, 0}, {1, 1}, {0, 1}, {-1, 1},
    {-1, 0}, {-1, -1}, {0, -1}, {1, -1}
};

bool dentroDosLimites(int x, int y) {
    return x >= 0 && x < linha && y >= 0 && y < coluna;
}

void procura(int x, int y, int cont) {
    if (matrix[x][y] == '#') {
        matrix[x][y] = cont;

        for (int i = 0; i < 8; i++) {
            int newX = x + movimentos[i][0];
            int newY = y + movimentos[i][1];

            if (dentroDosLimites(newX, newY) && matrix[newX][newY] == '#') {
                procura(newX, newY, cont);
            }
        }
    }
}

int main() {
    cin >> linha >> coluna;
    matrix.assign(linha, vector<char>(coluna));

    for (int i = 0; i < linha; i++) {
        for (int j = 0; j < coluna; j++) {
            cin >> matrix[i][j];
        }
    }

    int cont = 0;

    for (int i = 0; i < linha; i++) {
        for (int j = 0; j < coluna; j++) {
            if (matrix[i][j] == '#') {
                procura(i, j, ++cont);
            }
        }
    }

    cout << cont << endl;

    return 0;
}
