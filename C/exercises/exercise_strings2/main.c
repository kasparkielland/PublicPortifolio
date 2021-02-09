#include <stdio.h>
#include <string.h>

int main() {
    char string1[] = "Hello, World!";
    size_t fullSize = strlen(string1);
    int parts = 13;
    size_t partSize = strlen(string1) / parts;

    for (int i = 1; i <= parts; i++){
        printf("\n%d/%i of the string is: \n", i, parts);

        for (int pos = (i - 1) * partSize; pos < i * partSize; pos++) {
            printf("%c", string1[pos]);
        }
    }

    printf("\nThe rest of the string is: \n");

    for (int pos = fullSize - fullSize % parts; pos < fullSize; pos++){
        printf("%c", string1[pos]);
    }
    return 0;
}