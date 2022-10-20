// gcc bof_3.c -o bof_3 -g -fno-stack-protector -no-pie

#include <stdio.h>

int vuln() {
    char name[1000];

    printf("%s", "Enter your name: ");
    fgets(name, 0x1000, stdin);
    
    printf("Hello, %s", name);

    return 0;
}

int main() {
    // Disable buffering.
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);

    puts("Here are some things to help:");
    printf("puts: %p\n", puts);
    printf("printf: %p\n", printf);
    printf("setvbuf: %p\n", setvbuf);

    return vuln();
}
