#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *temp;
	int is_palindrome = 1;

	if (*head == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		temp = slow;
		slow = slow->next;
		temp->next = prev;
		prev = temp;
	}

	if (fast != NULL)
		slow = slow->next;

	while (slow != NULL && is_palindrome)
	{
		if (slow->n != prev->n)
			is_palindrome = 0;
		slow = slow->next;
		prev = prev->next;
	}

	return (is_palindrome);
}
