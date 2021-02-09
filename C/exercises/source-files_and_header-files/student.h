//
// Created by Kaspar Kielland on 01.11.2017.
//

#ifndef SOURCE_FILES_AND_HEADER_FILES_STUDENT_H
#define SOURCE_FILES_AND_HEADER_FILES_STUDENT_H

// Struct definitions
typedef struct {
    int id;
    char name[200];
    char adress[200];
} student_t;

// Function decelerations

void print_student(student_t student);
student_t read_student();

#endif //SOURCE_FILES_AND_HEADER_FILES_STUDENT_H
