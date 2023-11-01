#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: Pointer to the head of the sorted list.
 * @number: Integer to be inserted.
 * Return: Address of the new node or NULL on failure.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current, *prev;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}

	new_node->n = number;
	new_node->next = NULL;

	current = *head;
	prev = NULL;
	while (current != NULL && current->n < number)
	{
		prev = current;
		current = current->next;
	}

	if (prev == NULL)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		prev->next = new_node;
		new_node->next = current;
	}
	return (new_node);
}
