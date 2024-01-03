#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - Inserts a new node into a sorted linked list
 * @head: Pointer to the head of the linked list
 * @number: Value to be inserted into the linked list
 *
 * Return: Pointer to the head of the modified linked list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *temp;

	newnode = (listint_t *)malloc(sizeof(listint_t));

	if (newnode == NULL)
		return (NULL);

	temp = *head;

	newnode->n = number;
	newnode->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		newnode->next = *head;
		*head = newnode;
		return (*head);
	}

	while (temp->next != NULL && number > temp->next->n)
		temp = temp->next;

	newnode->next = temp->next;
	temp->next = newnode;
	return (*head);
}
