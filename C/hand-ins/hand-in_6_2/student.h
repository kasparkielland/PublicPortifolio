//
// Created by Kaspar Kielland on 23.11.2017.
//

#ifndef HAND_IN_6_2_STUDENT_H
#define HAND_IN_6_2_STUDENT_H

struct Student{
    char name[100];
    int age;
    int totalStudents;
};

struct Student* get_student();
void read_student(int i, struct Student* myStudentP);
void printAll(struct Student* student, int count);
void printYoungest(struct Student* student, int count);
void printOldest(struct Student* student, int count);

#endif //HAND_IN_6_2_STUDENT_H
