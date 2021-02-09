#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define STRING_LENGTH 200


int main() {
    //Allocate space for string
    char string1[STRING_LENGTH] = { 0 };
    char string2[STRING_LENGTH] = { 0 };
    char string3[STRING_LENGTH * 2] = { 0 };

    //Read in the first string
    fgets(string1, STRING_LENGTH, stdin);
    string1 [strlen(string1) -1] = 0;

    //Read in the second string
    fgets(string2, STRING_LENGTH, stdin);
    string2 [strlen(string2) -1] = 0;

    //Copy both strings to string3
    strcat(string3, string1);
    strcat(string3, string2);

    string3[5] += 10;
    string3[5] -= 10;

    //Print the characters stored in string 3
    for (size_t i = 0; i < strlen(string3); i++){
        printf("%c | ", tolower(string3[i]));
    }
    printf("\n");


    //Check if the string are equal
    if (strcmp(string1, string2) == 0){
        printf("Strins are equal\n");

    }
    else{
        printf("String are not equal\n");
    }
    return 0;
}