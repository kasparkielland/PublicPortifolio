#ifndef HAND_IN_5_2_STUDENT_H
#define HAND_IN_5_2_STUDENT_H
//Defineing a struct for student
typedef struct {
    int ID;
    int age;
    char name[100];
} student_t;

//Calling the functions that is going to be needed
void print_student(student_t student);
student_t read_student();
void write_studentToFile(student_t student);
student_t read_studentFromFile();

#endif //HAND_IN_5_2_STUDENT_H
