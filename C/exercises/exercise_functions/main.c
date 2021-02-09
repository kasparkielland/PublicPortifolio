#include <stdio.h>

int sum(int num1, int num2);
void print(int numbers[], int count);

int main() {
    printf("Hello, World!\n");

    int result = sum(2,2);
    printf("2 + 2 is %i\n", result);

    int values[5] = {1, 2, 3, 4, 5 };
    print(values, 5);

    return 0;
}


int sum(int num1, int num2){
    int result = num1 + num2;
    return result;
}

void print(int numbers[], int count){
    for (int i = 0; i < count; i++){
        printf("Number %i is % i\n", i, numbers[i]);
    }
}

