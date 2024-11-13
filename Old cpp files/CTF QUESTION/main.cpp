// MOVE THIS FILE TO MAIN PC
// ASK MOM FOR FLASHDRIVE

#include <iostream>
#include <stdio.h>
#include <string.h>

void hidden_function() {
    printf("Congrats! You've triggered the hidden function and obtained the flag!\n");
    //Replace flag_goes_here with the flag and the gimic behind the flag
    printf("CTF{flag_goes_here}\n");
}

void vulnerable_function(char *input) {
char buffer[64];
strcpy(buffer, input);
printf("Input: %s\n", buffer);
}

int main(int argc, char **argv) {
    if (argc != 2) {
        printf("Usage: %s <input>\n", argv[0]);
        return 1;
    }

}

vulnerable_fuction(argv[1]);

return 0;