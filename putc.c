#include <stdio.h>

int main(int argc, char *argv[])
{

                          FILE *fp1;
                          fp1 = open("nixa.txt", "w");

                          fprintf(fp1, "%s %s", " We ", "are", "Awesome");
                          fclose(fp1);
}