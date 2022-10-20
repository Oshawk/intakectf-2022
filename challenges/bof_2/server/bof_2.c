// gcc bof_2.c -o bof_2 -g -fno-stack-protector -no-pie

#include <stdio.h>

__attribute__((force_align_arg_pointer))
int win() {
    FILE *flag_file = fopen("flag.txt", "r");

    if (flag_file == NULL) {
        puts("Error opening flag.");
        return 1;
    }

    char flag[23];
    fgets(flag, sizeof(flag), flag_file);

    puts(flag);

    return 0;
}

int vuln() {
    char name[100];

    printf("%s", "Enter your name: ");
    fgets(name, 0x100, stdin);
    
    printf("Hello, %s", name);

    return 0;
}

int main() {
    // Disable buffering.
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);

    return vuln();
}
