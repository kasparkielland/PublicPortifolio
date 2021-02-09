#include <stdio.h>
#include <string.h>

#include "student.h"
//This function prints out the student information
void print_student(student_t student){
    printf("Student id: %i\n", student.ID);
    printf("Name: %s", student.name);
    printf("Age: %i\n", student.age);
}

//This function reads in the student information given by the user, and returns
student_t read_student(){
    student_t student;

    printf("Student id: ");
    scanf("%i", &student.ID);
    getchar();

    printf("Name: ");
    fgets(student.name, 100, stdin);
    student.name[strlen(student.name)-1] = 0;

    printf("Age: ");
    scanf("%i", &student.age);

    return student;
}

void write_studentToFile(student_t student){

    FILE* f = fopen("student_write.txt", "w");

    fprintf(f, "%i\n%s\n%i\n", student.ID, student.name, student.age);

    fclose(f);
}

student_t read_studentFromFile(){
    student_t student;

    FILE* f = fopen("student_read.txt", "r");

    while (!feof(f)){
        fscanf(f, "%i", &student.ID);
        fgetc(f);

        fgets(student.name, 100, f);

        fscanf(f, "%i", &student.age);
        fgetc(f);
        }

    fclose(f);

    return student;
}