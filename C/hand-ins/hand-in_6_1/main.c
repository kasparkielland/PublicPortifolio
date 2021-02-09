#include <stdio.h>
#include <stdlib.h>

void sort(int* array, int count);
void print_numbers(int count, int* array);

int main() {
    int count;

    scanf("%i", &count);

    if (count > 0) {
        int* numbers = malloc(count * sizeof(int));

        for (int i = 0; i < count; i++) {
            printf("Enter value %i: ", (i + 1));
            scanf("%i", &numbers[i]);
            getchar();
        }

        print_numbers(count, numbers);
        free(numbers);
        numbers = NULL;
    }
    else
        printf("\nNo numbers were given\n");

    return 0;
}

void print_numbers(int count, int* array){

    printf("\nCount: %i", count);

    printf("\nNumbers: ");
    for (int i = 0; i < count; i++) {
        printf("%i ", array[i]);
    }

    sort(array, count);

    printf("\nSorted: ");
    for (int i = 0; i < count; ++i) {
        printf("%i ", array[i]);
    }

    printf("\n");
}

void sort(int* arrayToSort, int count){
    int tempHolder;

    for (int i = 0; i < count; i++) {
        for (int j = i + 1; j < count; j++) {
            if (arrayToSort[i] > arrayToSort[j]) {
                tempHolder = arrayToSort[i];
                arrayToSort[i] = arrayToSort[j];
                arrayToSort[j] = tempHolder;
            }
        }
    }
}