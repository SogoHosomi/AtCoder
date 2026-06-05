#include <stdio.h>
#include <string.h>

typedef struct{
    char name[20];
    int rate;
} Player;

int main (void){
    int size = 0;
    Player player[20];

    FILE *f = fopen("rate.txt", "r");
    while (fscanf(f, "%s %d", player[size].name, &player[size].rate) == 2){
        size++;
    }
    fclose(f);

    char input[20];
    scanf("%s", input);

    for (int i = 0; i < size-1; i++){
        if(strcmp(input, player[i].name) == 0){
            printf("%d\n", player[i].rate);
            return 0;
        }
    }
    return 0;
}