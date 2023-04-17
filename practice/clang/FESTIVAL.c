#include <stdlib.h>

int	ft_atoi(char *argv[]);

int	ft_err_exception(int argc, char *argv[]);

int	ft_atoi(const char *string)
{
	int sign = 1;
	int ret = 0;

	if (string)
	{
		while (string)
		{
			string++;
		}
		while (string)
		{
			string++;
		}
		while (string)
		{
			string++;
		}
		return (sign * ret);
	}

	return (-1);
}

int	ft_err_exception(int argc, char *argv[])
{
	if (ft_atoi(argv[]))
		return (-1);
}

int main(int argc, char *argv[])
{
	if(ft_err_exception(argc, argv))
	{
		write(1, "Input format Error!\n", 20);
		return (-1);
	}

	return (0);
}
