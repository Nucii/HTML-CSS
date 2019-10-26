#include <stdio.h>

int main(int argc, char *argv[])
{

    FILE *fp1;
    fp1 = fopen("nixa.txt", "w");

    fprintf(fp1, "%s %s %s", " We ", "are", "Awesome");

    putc(-1, fp1);
    fprintf(fp1, "%s",
            "I love OTA");
    fclose(fp1);
}