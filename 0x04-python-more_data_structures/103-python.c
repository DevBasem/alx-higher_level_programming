#include <Python.h>
#include <bytesobject.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_bytes - Print information about a Python bytes object.
 *
 * This function prints the size, trying string, and the first 10 bytes of a Python bytes object.
 *
 * @p: Pointer to a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	int i;
	char *trying_str = NULL;
	long int size;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &trying_str, &size);

	printf("  size: %li\n", size);
	printf("  trying string: %s\n", trying_str);
	if (size < 10)
		printf("  first %li bytes:", size + 1);
	else
		printf("  first 10 bytes:");
	for (i = 0; i <= size && i < 10; i++)
		printf(" %02hhx", trying_str[i]);
	printf("\n");
}

/**
 * print_python_list - Print information about a Python list.
 *
 * This function prints the size, allocated memory, and elements' types of a Python list.
 * If an element is of type "bytes," it calls print_python_bytes to provide more information.
 *
 * @p: Pointer to a Python list object
 */
void print_python_list(PyObject *p)
{
	long int size = PyList_Size(p);
	int i;
	PyListObject *list = (PyListObject *)p;
	const char *type;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", list->allocated);
	for (i = 0; i < size; i++)
	{
		type = (list->ob_item[i])->ob_type->tp_name;
		printf("Element %i: %s\n", i, type);
		if (!strcmp(type, "bytes"))
			print_python_bytes(list->ob_item[i]);
	}
}
