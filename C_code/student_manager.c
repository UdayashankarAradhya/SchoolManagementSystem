#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_STUDENTS 100

typedef struct {
    char name[50];
    int roll;
    char course[50];
} Student;

Student students[MAX_STUDENTS];
int count = 0;

void add_student(char *name, int roll, char *course) {
    if (count >= MAX_STUDENTS) {
        printf("❌ Student list full.\n");
        return;
    }
    // Check if roll already exists
    for (int i = 0; i < count; i++) {
        if (students[i].roll == roll) {
            printf("❌ Roll number already exists.\n");
            return;
        }
    }
    strcpy(students[count].name, name);
    students[count].roll = roll;
    strcpy(students[count].course, course);
    count++;
    printf("✅ Student added successfully.\n");
}

void view_student() {
    if (count == 0) {
        printf("❌ No students added yet.\n");
        return;
    }
    for (int i = 0; i < count; i++) {
        printf("👤 Name: %s\n", students[i].name);
        printf("🆔 Roll: %d\n", students[i].roll);
        printf("📚 Course: %s\n", students[i].course);
        printf("-----------------\n");
    }
}

void delete_student(int roll) {
    int found = 0;
    for (int i = 0; i < count; i++) {
        if (students[i].roll == roll) {
            found = 1;
            for (int j = i; j < count - 1; j++) {
                students[j] = students[j + 1];
            }
            count--;
            printf("✅ Student deleted successfully.\n");
            break;
        }
    }
    if (!found) {
        printf("❌ Student not found.\n");
    }
}

void find_by_roll(int roll) {
    for (int i = 0; i < count; i++) {
        if (students[i].roll == roll) {
            printf("👤 Name: %s\n", students[i].name);
            printf("🆔 Roll: %d\n", students[i].roll);
            printf("📚 Course: %s\n", students[i].course);
            return;
        }
    }
    printf("❌ Student not found.\n");
}

void find_by_name(char *name) {
    int found = 0;
    for (int i = 0; i < count; i++) {
        if (strcmp(students[i].name, name) == 0) {
            printf("👤 Name: %s\n", students[i].name);
            printf("🆔 Roll: %d\n", students[i].roll);
            printf("📚 Course: %s\n", students[i].course);
            found = 1;
        }
    }
    if (!found) {
        printf("❌ Student not found.\n");
    }
}

void list_by_course(char *course) {
    int found = 0;
    for (int i = 0; i < count; i++) {
        if (strcmp(students[i].course, course) == 0) {
            printf("👤 Name: %s\n", students[i].name);
            printf("🆔 Roll: %d\n", students[i].roll);
            printf("-----------------\n");
            found = 1;
        }
    }
    if (!found) {
        printf("❌ No students found in this course.\n");
    }
}

void count_students() {
    printf("📊 Total students: %d\n", count);
}

void update_student(int roll, char *new_name, char *new_course) {
    for (int i = 0; i < count; i++) {
        if (students[i].roll == roll) {
            strcpy(students[i].name, new_name);
            strcpy(students[i].course, new_course);
            printf("✅ Student updated successfully.\n");
            return;
        }
    }
    printf("❌ Student not found.\n");
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("❌ No option provided.\n");
        return 1;
    }

    // Preload some students for testing if you want, or leave empty
    // Example:
    // add_student("Nikhil", 123, "ECE");
    // add_student("Jay", 179, "CSE");

    char *option = argv[1];

    if (strcmp(option, "1") == 0) {  // Add Student
        if (argc < 5) {
            printf("❌ Usage: 1 <name> <roll> <course>\n");
            return 1;
        }
        char *name = argv[2];
        int roll = atoi(argv[3]);
        char *course = argv[4];
        add_student(name, roll, course);

    } else if (strcmp(option, "2") == 0) {  // View Students
        view_student();

    } else if (strcmp(option, "3") == 0) {  // Delete Student
        if (argc < 3) {
            printf("❌ Usage: 3 <roll>\n");
            return 1;
        }
        int roll = atoi(argv[2]);
        delete_student(roll);

    } else if (strcmp(option, "4") == 0) {  // Find by Roll
        if (argc < 3) {
            printf("❌ Usage: 4 <roll>\n");
            return 1;
        }
        int roll = atoi(argv[2]);
        find_by_roll(roll);

    } else if (strcmp(option, "5") == 0) {  // Find by Name
        if (argc < 3) {
            printf("❌ Usage: 5 <name>\n");
            return 1;
        }
        find_by_name(argv[2]);

    } else if (strcmp(option, "6") == 0) {  // List by Course
        if (argc < 3) {
            printf("❌ Usage: 6 <course>\n");
            return 1;
        }
        list_by_course(argv[2]);

    } else if (strcmp(option, "7") == 0) {  // Count Students
        count_students();

    } else if (strcmp(option, "8") == 0) {  // Update Student
        if (argc < 5) {
            printf("❌ Usage: 8 <roll> <new_name> <new_course>\n");
            return 1;
        }
        int roll = atoi(argv[2]);
        char *new_name = argv[3];
        char *new_course = argv[4];
        update_student(roll, new_name, new_course);

    } else {
        printf("❌ Invalid option.\n");
    }

    return 0;
}
