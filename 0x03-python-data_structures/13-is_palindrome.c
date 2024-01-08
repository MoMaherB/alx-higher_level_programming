#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - Check if a linked list of integers is a palindrome.
 * @head: Double pointer to the head of the linked list.
 * Return: 1 if the linked list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current , *nextptr, *reverse = NULL, *temp, *newnode;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	current = nextptr = *head;

	while (nextptr != NULL && nextptr->next != NULL)
	{
		nextptr = nextptr->next->next;
		newnode = (listint_t *)malloc(sizeof(listint_t));
		newnode->n = current->n;
		newnode->next = reverse;
		reverse = newnode;
		current = current->next;
	}

	temp = reverse;

	if (nextptr != NULL)
		current = current->next;

	while (current != NULL)
	{
		if (reverse->n != current->n)
		{
			reverse = temp;
			while(temp != NULL)
			{
				temp = temp->next;
				free(reverse);
				reverse = temp;
			}
			return (0);
		}
		reverse = reverse->next;
		current = current->next;
	}

	reverse = temp;
	while (temp != NULL)
	{
		temp = temp->next;
		free(reverse);
		reverse = temp;
	}
	return (1);
}
