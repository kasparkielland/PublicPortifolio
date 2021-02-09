//
// Created by Kaspar Kielland on 23.11.2017.
//

#include <stdio.h>
#include <memory.h>

#include "student.h"

void printAll(struct Student* student, int count){
    printf("\nCount: %i\n", count);
    for (int i = 0; i < count; i++){
        printf("Name = %s, Age = %i\n", student[i].name, student[i].age);
    }
}

void printYoungest(struct Student* student, int count){
    char youngestName[100];
    strcpy(youngestName, student[0].name);
    int youngestAge = student[0].age;

    for (int i = 0; i < count; i++) {
        if (student[i].age < youngestAge){
            strcpy(youngestName, student[i].name);
            youngestAge = student[i].age;
        }
    }

    printf("Youngest: %s\n", youngestName);
}

void printOldest(struct Student* student, int count){
    char oldestName[100];
    strcpy(oldestName, student[0].name);
    int youngestAge = student[0].age;

    for (int i = 0; i < count; i++) {
        if (student[i].age > youngestAge){
            strcpy(oldestName, student[i].name);
            youngestAge = student[i].age;
        }
    }

    printf("Oldest: %s\n", oldestName);
}