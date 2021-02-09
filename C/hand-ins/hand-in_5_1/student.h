#ifndef HAND_IN_5_1_STUDENT_H
#define HAND_IN_5_1_STUDENT_H

typedef struct {
    int studentID;
    int age;
    char name[100];
} student_t;

void print_student(student_t student);
student_t read_student();


#endif //HAND_IN_5_1_STUDENT_H
