#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *temp, *fptr, *lptr;
	int half_way, count = 0, i = 1, j = 1;

	if (*head == NULL)
		return (1);
	temp = *head;

	while(temp != NULL)
	{
		count++;
		temp = temp -> next;
	}

	if (count == 1)
		return (1);
	fptr = lptr = *head;
	half_way = count / 2;

	while (i <= half_way)
	{
		while(j < count)
		{
			lptr = lptr -> next;
			j++;
		}
		if (fptr -> n != lptr -> n)
			return (0);
		fptr = fptr -> next;
		lptr = *head;
		i++;
		j = 1;
		count--;
	}

	return (1);
}
