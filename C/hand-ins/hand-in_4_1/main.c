#include <stdio.h>
#include <string.h>

#define STRING_LENGTH 30

int main() {

    char word[STRING_LENGTH] = { 0 };
    char revWord[STRING_LENGTH] = { 0 };
    int j = 0;

    printf("Enter your word: ");
    fgets(word, STRING_LENGTH, stdin);
    word[strlen(word) -1] = 0;
    size_t length = strlen(word);

    for (int i = length -1; i >= 0; i--){
        revWord[j] = word[i];
        j++;
    }
    revWord[j] = '\0';

    printf("The word contains %zu letters \n", length);
    if (strcmp(word, revWord) == 0){
        printf("The word is a palindrome\n");
    }
    else{
        printf("The word is not a palindrome\n");
    }

    printf("The word reversed is '%s'\n", revWord);

    return 0;
}