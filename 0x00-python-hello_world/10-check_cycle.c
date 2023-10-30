#include "lists.h"

/**
 * check_cycle - Checks for a cycle in a singly linked list.
 * @list: A pointer to the head of the linked list.
 * Return: 1 if a cycle is detected, 0 if there is no cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}

	return (0);
}
