#include <stdio.h>

int main() {
    int classObtained, failedSubjects;
    int grace = 0;

    printf("Enter class obtained (1 for First, 2 for Second, 3 for Third): ");
    scanf("%d", &classObtained);

    printf("Enter number of subjects failed: ");
    scanf("%d", &failedSubjects);

    switch (classObtained) {
        case 1:  // First class
            if (failedSubjects > 3)
                grace = 0;
            else
                grace = failedSubjects * 5;
            break;

        case 2:  // Second class
            if (failedSubjects > 2)
                grace = 0;
            else
                grace = failedSubjects * 4;
            break;

        case 3:  // Third class
            if (failedSubjects > 1)
                grace = 0;
            else
                grace = 5;   // Fixed 5 marks
            break;

        default:
            printf("Invalid class entered.\n");
            return 0;
    }

    printf("Grace marks awarded: %d\n", grace);
    return 0;
}
