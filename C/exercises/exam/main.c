#include <stdio.h>
#include <memory.h>
#include <stdlib.h>


struct student
{
    char name[20];
    int age; };

int main() {
        int i = 0;
        do
        {
            i++;
            if (i == 2)
                continue;
            printf("In while loop ");
        } while (i < 2);
        printf("%d\n", i);


    for (i = 0; i < 10; i++) { }
    printf("%i", i);

    double d; scanf("%d", &d);

    int number;

    FILE* f = fopen("hello.txt", "r");
    fscanf("%i", &number);

    return 0;

}


