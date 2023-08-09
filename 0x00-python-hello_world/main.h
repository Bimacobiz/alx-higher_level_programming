#ifndef MAIN_H
#define MAIN_H
#include <stdlib.h>
/**
 * struct listint_s - singly linked list
 * @s: an integer
 * @next: a pointer to the next node
 *
 * Description: this is a node for the singly linked list
 * for Holberton project
 */
typedef struct listint_s
{
	int s;
	struct listint_s *next;
} listint_t;
int check_cycle(listint_t *list);
listint_t *add_nodeint(listint_t **head, const int n);
size_t print_listint(const listint_t *h);
void free_listint(listint_t *head);
#endif
