#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int student_id;

void secret_function() {
    char *phone = getenv("PHONE");
    if(!phone) {
        printf("PHONE env variable not set!\n");
        return;
    }
    printf("my phone is %s\n", phone);
}

void vuln() {
    char buffer[32];
    printf("type something:\n");
    gets(buffer);
    printf("you typed: %s\n", buffer);
    printf("student id now: %d\n", student_id);
}

int main() {
    char *sid = getenv("STUDENT_ID");
    if(sid)
        student_id = atoi(sid);
    else
    return;

    printf("id before exploit: %d\n", student_id);
    vuln();
    return 0;
}