#include <iostream>
#include <vector>
#include <queue>

using namespace std;

void procura(int x, int y, vector<vector<char>>& matrix, int& cont, int linha, int coluna) {
    int vetX[] = {1, 1, 0, -1, -1, 0, 1, -1};
    int vetY[] = {0, 1, 1, 1, 0, -1, -1, -1};

    if (matrix[x][y] == '#') {
        cont++;
        matrix[x][y] = '0' + cont;

        queue<pair<int, int>> q;
        q.push(make_pair(x, y));

        while (!q.empty()) {
            pair<int, int> curr = q.front();
            q.pop();

            for (int c = 0; c < 8; c++) {
                int newX = curr.first + vetX[c];
                int newY = curr.second + vetY[c];

                if (newX >= 0 && newX < linha && newY >= 0 && newY < coluna && matrix[newX][newY] == '#') {
                    q.push(make_pair(newX, newY));
                    matrix[newX][newY] = '0' + cont;
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

    for (int i = 0; i < linha; i++) {
        for (int j = 0; j < coluna; j++) {
            if (matrix[i][j] == '#') {
                procura(i, j, matrix, cont, linha, coluna);
            }
        }
    }

    cout << cont << endl;

    return 0;
}
