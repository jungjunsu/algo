#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
	int a = 0;
	int b = 0;

	if (argc != 3)
		return (-1);
	a = atoi(argv[1]);
	b = atoi(argv[2]);
	if ((a <= 0) || (b >= 10))
		return (-1);
	printf("%d", a + b);

	return (0);
}
