#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    char a;

    scanf("%c", &a);
    
    if(a >= 'U')
        a --;
    if(a >= 'O')
        a --;
    if(a >= 'I')
        a --;
    if(a >= 'E')
        a --;
    if(a >= 'A')
        a --;

    printf("%d\n", a - 64);

}