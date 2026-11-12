#include <stdio.h>

int main(void) {
    int price = 2500;
    printf("price is %d\n", price);
    printf("price lives at address %p\n", (void *)&price);
    return 0;
}
