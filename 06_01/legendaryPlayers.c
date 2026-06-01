#include <stdio.h>
#include <string.h>

typedef struct {
    char name[20];
    int rate;
} Player;

int main() {
    Player players[100];
    int size = 0;

    FILE *f = fopen("rate.txt", "r");
    while (fscanf(f, "%s %d", players[size].name, &players[size].rate) == 2) {
        size++;
    }
    fclose(f);

    char query[20];
    scanf("%s", query);

    for (int i = 0; i < size; i++) {
        if (strcmp(players[i].name, query) == 0) {
            printf("%d\n", players[i].rate);
            return 0;
        }
    }

    return 0;
}
