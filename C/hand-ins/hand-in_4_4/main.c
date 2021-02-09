#include <stdio.h>
#include <memory.h>

#define STRING_LENGTH 50


int main() {
    char string[STRING_LENGTH] = { 0 };
    char stringDuplicate[STRING_LENGTH] = { 0 };

    int count = 0;

    fgets(string, STRING_LENGTH, stdin);

    string[strlen(string)-1] = 0;
    strcpy(stringDuplicate, string);

    int stringLength = strlen(string);

    for (int i=0; i < stringLength; i++ ){
        for (int j = 0; j < stringLength; j++) {
            if (string[i] == stringDuplicate[j]) {
                count++;
                stringDuplicate[j] = 0;
            }
        }
        if (count != 0) {
            printf("'%c' : %i\n", string[i], count);
            count = 0;
        }
    }

    return 0;
}
