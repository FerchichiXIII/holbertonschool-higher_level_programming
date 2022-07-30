#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 * Return: 1 if palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL && head == NULL)
		return (1);
	return (check_palindrome(head, *head));
}

/**
 * check_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 * @last: pointer to pointer of first node of listint_t list
 * Return: 1 if palindrome, 0 if not
 */

int check_palindrome(listint_t **head, listint_t *last)
{
	if (last == NULL)
		return (1);
	if (check_palindrome(head, last->next) && (*head)->n == last->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
