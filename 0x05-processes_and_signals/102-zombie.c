#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
/**
 * infinite_while - sleeping beauty
 * Return: 0 always
 */
int infinite_while(void)
{
	while (1)
		sleep(1);
	return (0);
}

/**
 * main - Main Entry point
 * Return: 0 on success
*/
int main(void)
{
	int i = 0;

	while (i < 5)
	{
		if (fork() == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
		i++;
	}
	infinite_while();
	return (0);
}
