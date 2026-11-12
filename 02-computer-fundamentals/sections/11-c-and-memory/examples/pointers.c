#include <stdio.h>

int main(void) {
    int price = 2500;
    int *p = &price;       // p holds the address of price
    printf("value through pointer: %d\n", *p);
    *p = 3000;             // change price via the pointer
    printf("price is now: %d\n", price);
    return 0;
}
