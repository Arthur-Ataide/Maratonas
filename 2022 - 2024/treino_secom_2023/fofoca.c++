#include <iostream>
#include <queue>
 
using namespace std;
 
void showpq(priority_queue<int> gq)
{
    priority_queue<int> g = gq;
    while (!g.empty()) {
        cout << '\t' << g.top();
        g.pop();
    }
    cout << '\n';
}

int main(){
    priority_queue<int> fila;
    int n, cont, aux, a, b, c;

    cont = 0;
    cin >>  n;

    for(int i = 0; i < n; i++){
        cin >> aux;
        if (aux != 0)
            fila.push(aux);
    }

    while (fila.size() > 1){

        // showpq(fila);
        
        a = fila.top();
        fila.pop();

        b = fila.top();
        fila.pop();

        c = 0;
        c = fila.top();

        aux = b - c;

        if (b != 1){
            a -= aux + 1;
            b -= aux + 1;
            cont += aux + 1;
        }
        
        else{
            a --;
            b --;
            cont ++;
        }
        
        // cout << a << endl;
        // cout << b << endl;

        if (a != 0){
            fila.push(a);
            if (b != 0)
                fila.push(b);
        }

    }
    

    

    cout << cont << endl;
}