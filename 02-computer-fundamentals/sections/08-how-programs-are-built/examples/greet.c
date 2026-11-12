#include <stdio.h>

int add(int a, int b) {
    return a + b;
}

int main(void) {
    printf("Mina Coffee\n");
    printf("2 lattes = %d coffees\n", add(1, 1));
    return 0;
}
