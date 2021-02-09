#include <stdio.h>

int main(void){
    float numbers[100];
    float sum = 0;
    float count = 0;
    float average = 0;


    for (int i = 0; i <= sizeof(numbers); i++){
        printf("Please enter a number: ");
        scanf("%g", &numbers[i]);

        sum = sum + numbers[i];

        if (numbers[i] == 0){
            i = sizeof(numbers);
            average = sum/count;
            printf("You entered 0. The program has ended.\n\n");
            printf("Sum: %g\n", sum);
            printf("Count: %g\n", count);
            printf("Average: %g\n", average);
        }
        count++;

    }

    return 0;
}