#include <iostream>
#include <vector>

using namespace std;

int linha, coluna;
vector<vector<char>> matrix;
vector<vector<bool>> visited;

void procura(int x, int y) {
    int vetX[] = {1, 1, 0, -1, -1, 0, 1, -1};
    int vetY[] = {0, 1, 1, 1, 0, -1, -1, -1};
    
    visited[x][y] = true;


    for (int c = 0; c < 8; c++) {
        int newX = x + vetX[c];
        int newY = y + vetY[c];

        if (newX >= 0 && newX < (linha) && newY >= 0 && newY < (coluna) &&  matrix[newX][newY] == '#' && !visited[newX][newY]) {
            procura(newX, newY);
        }
    }

}

int main() {
    cin >> linha >> coluna;
    matrix.assign(linha, vector<char>(coluna));
    visited.assign(linha, vector<bool>(coluna, false));

    for (int i = 0; i < linha; i++) {
        for (int j = 0; j < coluna; j++) {
            cin >> matrix[i][j];
        }
    }

    int cont = 0;

    for (int i = 0; i < linha; i++) {
        for (int j = 0; j < coluna; j++) {
            if (matrix[i][j] == '#' && !visited[i][j]) {
                cont++;
                procura(i, j);
            }
        }
    }

    cout << cont << endl;

    return 0;
}