#include <stdio.h>

int main() {
    const int size = 6;
    int numbers[size] = {0};

    printf("Starting values:\n");
    for (int i = 0; i < size; i++){
        printf("Number %i is: %i\n", i, numbers[i]);
    }

    printf("\n");

    printf("Changed values: \n");
    for (int i = 0; i < size; i++){
        numbers[i] = i + 5;
        printf("numbers %i is: %i\n", i , numbers[i]);
    }


    return 0;
}