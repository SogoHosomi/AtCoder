#include <stdio.h>

int main(){
    int a, b;
    int tmp = 1;
    int sum = 1;
    scanf("%d%d", &a, &b);
    for (int i = 0; i < a; i++){
        tmp *= b;
    }
    for (int j = 0; j < b; j++){
        sum *= a;
    }
    sum += tmp;
    printf("%d\n", sum);

    return 0;
}