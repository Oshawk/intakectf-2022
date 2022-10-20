// gcc simple_linux.c -o simple_linux
// flag{e3e0a68e96aa46bf}

#include <stdio.h>
#include <string.h>

int main() {
    char part_one[22] = {180, 3, 53, 71, 197, 95, 52, 161, 71, 57, 98, 24, 161, 197, 12, 184, 253, 69, 29, 198, 251, 196};
    char part_two[22] = {210, 111, 84, 32, 190, 58, 7, 196, 119, 88, 84, 32, 196, 252, 58, 217, 156, 113, 43, 164, 157, 185};
    char result[22];

    for (int i = 0; i < sizeof(part_one); i++) {
        result[i] = part_one[i] ^ part_two[i];
    }

    char password[sizeof(part_one) + 1];
    printf("%s", "Enter the password: ");
    fgets(password, sizeof(part_one) + 1, stdin);

    if (memcmp(result, password, sizeof(part_one))) {
        puts("Wrong :(");
    } else {
        puts("Correct!");
    }

    return 0;
}
