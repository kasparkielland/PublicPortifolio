#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define STRING_LENGTH 20

int main() {
    char string[STRING_LENGTH] = { 0 };
    char string2[STRING_LENGTH] = { 0 };
    char UPPERstring[STRING_LENGTH] ={ 0 };
    char LOWERstring[STRING_LENGTH] ={ 0 };

    printf("Enter string: ");
    fgets(string, STRING_LENGTH, stdin);
    string[strlen(string)-1] = 0;

    for (int i = 0; string[i] != '\0'; i++){
        UPPERstring[i] = toupper(string[i]);
    }
    printf("The string in uppercase is '%s'\n", UPPERstring);

    for (int i = 0; string[i] != '\0'; i++){
        LOWERstring[i] = tolower(string[i]);
    }
    printf("The string in lowercase is '%s'\n", LOWERstring);

    int length = strlen(string);
    int halfLength = length/2;

    for (int i = halfLength; i < length; i++){
        string2[i - halfLength] = string[i];
        string[i] = '\0';
    }

    printf("The string in split is '%s - %s'", string, string2);

    return 0;
}