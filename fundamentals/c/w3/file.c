#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int main(void) {
	FILE *f;
	f = fopen("file.txt", "a");
	fprintf(f, "Hello, file! \n");
	fclose(f);
}
