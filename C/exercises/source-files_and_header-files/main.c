#include <stdio.h>
#include <memory.h>

#include "student.h"

int main() {
    student_t student = read_student();

    print_student(student);

    return 0;
}