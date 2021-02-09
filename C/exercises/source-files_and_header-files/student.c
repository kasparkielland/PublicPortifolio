//
// Created by Kaspar Kielland on 01.11.2017.
//

#include <stdio.h>

#include "student.h"

void print_student(student_t student){
    printf("Id: %i\n", student.id);
    printf("Name: %s\n", student.name);
}

student_t read_student() {
    student_t s;

    scanf("%i", &s.id);
    getchar();

    fgets(s.name, 200, stdin);

    return s;
}

