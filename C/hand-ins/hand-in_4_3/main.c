#include <stdio.h>
#include <string.h>

#define STRING_LENGTH 20

int main() {
    char string1[STRING_LENGTH] = { 0 };
    char string2[STRING_LENGTH] = { 0 };

    fgets(string1, STRING_LENGTH, stdin);

    fgets(string2, STRING_LENGTH, stdin);

    string1[strlen(string1) - 1] = 0;
    string2[strlen(string2) - 1] = 0;

    if (strcmp(string1, string2) == 0){
        printf("are equal\n");
    }
    else{
        printf("are not equal\n");
    }

    if (strstr(string1, string2) != NULL || strstr(string2, string1) != NULL)
        printf("is a substring");
    else
        printf("is not a substring");


    return 0;
}