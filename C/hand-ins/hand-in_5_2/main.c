#include <stdio.h>
#include "student.h"

int main() {

    int selectedOption = 3;

    printf("\nWelcome!\n"
                   "\nThese are the menu options to choose from:\n\n"
                   "[1] - Reads student information from file\n"
                   "[2] - Writes student information to file\n"
                   "[3] - Exits program\n");

    while (selectedOption) {
        printf("\nEnter a menu option: ");

        scanf("%i", &selectedOption);
        printf("\n");

        if (selectedOption == 1)
            print_student(read_studentFromFile());

        else if (selectedOption == 2)
            write_studentToFile(read_student());

        else if (selectedOption == 3){
            printf("The program will now exit, bye bye!\n");
            return 0;
        }
        else
            printf("Wrong input, try again!");

    }
}