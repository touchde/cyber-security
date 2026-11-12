#include <stdio.h>
#include <string.h>

int main(void) {
    char name[8];                 // room for 7 letters + end marker
    strncpy(name, "Dara", sizeof(name) - 1);
    name[sizeof(name) - 1] = '\0';
    printf("hello, %s\n", name);
    return 0;
}
