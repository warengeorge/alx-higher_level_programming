#include <stdlib.h>
#include "lists.h"

/**
 * *insert_node - inserts number into a sorted singly linked list
 * @head: head of list
 * @number: integer to insert into a new node
 * Return: address of new node else NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *tmp;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	if (*head == NULL)
	{
		new_node->n = number;
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	else if (number <= (*head)->n)
	{
		new_node->n = number;
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	else
	{
		tmp = *head;
		while (tmp->next != NULL && number > tmp->next->n)
		{
			tmp = tmp->next;
		}
		new_node->n = number;
		new_node->next = tmp->next;
		tmp->next = new_node;
		return (new_node);
	}
	return (NULL);
}
