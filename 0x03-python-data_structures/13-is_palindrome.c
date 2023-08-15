#include "lists.h"
/**
 *reverse_listint - reverses a singly linked list
 *head: a pointer to a pointer to the first node of the given list
 *Return: a pointer to the head of the given linked list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *as_was = NULL;
	listint_t *present = *head;
	listint_t *next = NULL;

	while (present)
	{
		next = present->next;
		present->next = as_was;
		as_was = present;
		present = next;
	}

	*head = as_was;
	return(*head);
}

/**
 *is_palindrome - finds out if the linked list is a palindrome
 *@head: double points to the linked list provided
 *Return: 1 if it palindrome otherwise return 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head, *runner = *head, *temp = *head, *reversed = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		runner = runner->next->next;
		if (!runner)
		{
			reversed = current->next;
			break;
		}
		if (!runner->next)
		{
			reversed = current->next->next;
			break;
		}
		current = current->next;
	}

	reverse_listint(&reversed);

	while (reversed && temp)
	{
		if (temp->n == reversed->n)
		{
			reversed = reversed->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!reversed)
		return (1);

	return (0);
}
