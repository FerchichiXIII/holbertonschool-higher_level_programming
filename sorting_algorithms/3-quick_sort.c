#include "sort.h"
/**
 * quick_sort - Sorts an array of integers using the quick sort algorithm
 * @array: The array to be sorted
 * @size: Number of elements
 * Return: Nothing
 */

void quick_sort(int *array, size_t size)
{
	if (array == NULL || size < 2)
	{
		return;
	}
	for (int i = 0; i < size; i++)
	{
		for (int j = i + 1; j < size; j++)
		{
			if (array[i] > array[j])
			{
				int temp = array[i];
				array[i] = array[j];
				array[j] = temp;
			}
		}
	}
}
