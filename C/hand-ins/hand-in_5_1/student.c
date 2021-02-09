#include <stdio.h>
#include <string.h>

#include "student.h"

void print_student(student_t student){
    printf("\nStudent id: %i\n", student.studentID);
    printf("Name: %s\n", student.name);
    printf("Age: %i\n", student.age);
}

student_t read_student(){
    student_t student;

    printf("Student id: ");
    scanf("%i", &student.studentID);
    getchar();

    printf("Name: ");
    fgets(student.name, 100, stdin);
    student.name[strlen(student.name)-1] = 0;

    printf("Age: ");
    scanf("%i", &student.age);

    return student;
}

