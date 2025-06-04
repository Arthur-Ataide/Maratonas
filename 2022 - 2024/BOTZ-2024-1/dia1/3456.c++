#include <iostream> 
using namespace std; 

int main() 
{ 
    long long int N, aux, resto;
    cin >> N;
    


    while (1)
    {
        cout << N << endl;


        if (N >= 0 &&  N<= 9 )
        {
            return 0;
        }



        aux = N / 10;
        // cout << aux << endl;
        resto = N - aux*10;
        // cout << resto << endl;
        N = aux*3 + resto;
    }
    return 0;

}