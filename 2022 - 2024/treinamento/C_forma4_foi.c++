#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int linha, coluna;
vector<vector<char>> matrix;
vector<vector<bool>> visited;

int vetX[] = {1, 1, 0, -1, -1, 0, 1, -1};
int vetY[] = {0, 1, 1, 1, 0, -1, -1, -1};

void BFS(int x, int y, int cont) {
    queue<pair<int, int>> q;
    q.push({x, y});
    visited[x][y] = true;

    while (!q.empty()) {
        pair<int, int> curr = q.front();
        q.pop();

        for (int c = 0; c < 8; c++) {
            int newX = curr.first + vetX[c];
            int newY = curr.second + vetY[c];

            if (newX >= 0 && newX < linha && newY >= 0 && newY < coluna &&
                matrix[newX][newY] == '#' && !visited[newX][newY]) {
                q.push({newX, newY});
                visited[newX][newY] = true;
            }
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
                BFS(i, j, cont);
            }
        }
    }

    cout << cont << endl;

    return 0;
}