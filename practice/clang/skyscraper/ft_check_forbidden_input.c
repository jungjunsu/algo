#include <stdlib.h>

int ft_check_forbidden_input(int argc, char *argv[])
{
	if (argc > 3)
	{
		write(1, "arg count ERROR!\n", 17);
		return (-1);
	}
	else if (argc == 3)
	{
		/* ing. . .
		open cases.txt >
		find argc case from cases.txt > 
		check argc case >
		if check is good > 
		return argc case(can be changed format)
		else check is bad >
		return value is -1
		*/
		
		;
	}
	else
	{
		/* ing. . .
		check argc case > 
		if check is good >
		return argc case(can be changed format)
		else check is bad >
		return value is -1
		*/
		;
	}
}
