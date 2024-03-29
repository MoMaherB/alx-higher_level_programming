#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - Checks if a linked list has a cycle
 * @list: Pointer to the head of the linked list
 *
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *temp;

	if (list == NULL)
		return (0);
	temp = list;

	while (temp->next != NULL && temp->next != list)
		temp = temp->next;

	if (temp->next == list)
		return (1);


	return (0);
}
