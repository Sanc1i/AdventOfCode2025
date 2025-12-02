// puzzle_inline_asm.c
// clang -arch arm64 puzzle_inline_asm.c -o puzzle_inline_asm

#include <stdio.h>
#include <stdlib.h>

int rotation = 50;   // global, like the Python global
int output = 0;

void new_rotation(char *line) {
    int number = atoi(line + 1);   // parse substring from index 1
    char dir = line[0];

    if (dir == 'R') {
        // rotation += number; while(rotation > 99) rotation -= 100;
        __asm__ volatile (
            "add %w[rot], %w[rot], %w[num]\n\t"    // rot += num
            "1:\n\t"
            "cmp %w[rot], #99\n\t"
            "ble 2f\n\t"
            "sub %w[rot], %w[rot], #100\n\t"
            "b 1b\n\t"
            "2:\n\t"
            : [rot] "+r" (rotation)                // output + input
            : [num] "r" (number)
            : "cc", "memory"
        );
    } else {
        // rotation -= number; while(rotation < 0) rotation += 100;
        __asm__ volatile (
            "sub %w[rot], %w[rot], %w[num]\n\t"    // rot -= num
            "1:\n\t"
            "cmp %w[rot], #0\n\t"
            "bge 2f\n\t"
            "add %w[rot], %w[rot], #100\n\t"
            "b 1b\n\t"
            "2:\n\t"
            : [rot] "+r" (rotation)
            : [num] "r" (number)
            : "cc", "memory"
        );
    }
}

int main(void) {
    const char *filename = "puzzle.txt";
    FILE *f = fopen(filename, "r");
    if (!f) {
        puts("Could not open file");
        return 1;
    }

    char line[256];
    while (fgets(line, sizeof(line), f)) {
        new_rotation(line);
        if (rotation == 0) {
            output += 1;
        }
    }

    printf("%d\n", output);
    fclose(f);
    return 0;
}

