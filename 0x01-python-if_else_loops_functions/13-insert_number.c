#include "lists.h"

/**
 * insert_node - a function that nserts a number
 * into a linked list that ahs already been sorted.
 * @head: points to the linked list's head.
 * @number: The no. to insert
 *
 * Return: NULL in case of failure.
 * a pointer to the new node if successful.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *recent;

	recent = malloc(sizeof(listint_t));
	if (recent == NULL)
		return (NULL);
	recent->n = number;

	if (node == NULL || node->n >= number)
	{
		recent->next = node;
		*head = recent;
		return (recent);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	recent->next = node->next;
	node->next = recent;

	return (recent);
}
