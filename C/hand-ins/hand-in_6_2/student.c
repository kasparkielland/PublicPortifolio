//
// Created by Kaspar Kielland on 23.11.2017.
//

#include <stdio.h>
#include <memory.h>
#include <stdlib.h>

#include "student.h"

struct Student* get_student(){
    struct Student* pStudent = malloc(5 * sizeof(struct Student));

    int factor = 5;
    int i = 0;

    while (strcmp(pStudent[i-1].name, "stop") != 0 ) {
        if (i >= factor) {
            factor += 5;

            pStudent = realloc(pStudent, factor * sizeof(struct Student));
        }

        read_student(i, pStudent);
        i++;
    }
    i--;
    //Using 'totalStudents' in the struct 'Student' to preserve the total numbers of students given.
    // sizeof(student)/sizeof(student[0]) did not work...
    pStudent->totalStudents = i;

    return pStudent;

}

void read_student(int i, struct Student* myStudentP) {
    char tempName[100];

    printf("Enter student name here: ");
    fgets(tempName, 100, stdin);
    tempName[strlen(tempName) - 1] = '\0';
    strcpy(myStudentP[i].name, tempName);

    if (strcmp(tempName, "stop") == 0){
        return;
    }

    printf("Enter student age here: ");
    scanf("%i", &myStudentP[i].age);
    getchar();
}