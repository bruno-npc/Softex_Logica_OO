/******************************************************************************

Crie um vetor com ponteiros utilizando alocação dinâmica na linguagem C, que:
- use a função realloc;
- use a função sizeof;
- que tenha tamanho 22 de vetor;
- depois libere o bloco utilizando a função free.

*******************************************************************************/

#include <stdio.h>

int main()
{
    int* ptr;
    int i;
    
    ptr = (int*)malloc(22 * sizeof(int));
 
    if (ptr == NULL) {
        printf("Memoria nao alocada.\n");
        exit(0);
    }
    else {
        printf("Memoria alocada usando malloc.\n");

        printf("Elementos no array: ");
        for (i = 0; i < 22; ++i) {
            printf("%d, ", ptr[i]);
        }
        free(ptr);
        printf("Memoria liberada usando free.\n");
    }
    return 0;
}