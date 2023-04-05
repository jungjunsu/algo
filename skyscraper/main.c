int	ft_check_forbidden_input (int argc, char *argv[]);
void	skyscraper (int argc, char *argv[]);

int main(int argc, char *argv[])
{
	if (ft_check_forbidden_input(argc, argv))
		return (-1);
	skyscraper(argc, argv);
	return (0);
}
