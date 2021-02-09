#include <stdio.h>
#include <stdlib.h>

#include "student.h"

int main() {
    //The program will not print output in Bamboo if a printf() is not created at the beginning
    printf("Program: Hand-in_6_2\n"
                   "Made by: Kaspar E. Kielland at University of Agder 2017\n\n");

    struct Student* student = get_student();
    //Using 'totalStudents' in the struct 'Student' to preserve the total numbers of students given.
    // sizeof(student)/sizeof(student[0]) did not work...
    const int count = student->totalStudents;

    if (count != 0){
        printAll(student, count);
        printYoungest(student, count);
        printOldest(student, count);
    } else
        printf("\nNo students were given\n");


    free(student);
    student = NULL;

    return 0;
}