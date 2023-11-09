#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Print Python list info
 * @p: Pointer to a Python list object
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size = ((PyVarObject *)p)->ob_size;
	Py_ssize_t allocated = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = list->ob_item[i];
		PyTypeObject *type = item->ob_type;
		printf("Element %ld: %s\n", i, type->tp_name);
	}
}

/**
 * print_python_bytes - Print Python bytes object info
 * @p: Pointer to a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	Py_ssize_t size = ((PyVarObject *)p)->ob_size;
	char *str = bytes->ob_sval;

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	printf("  first 10 bytes: ");
	if (size > 10)
		size = 10;
	for (Py_ssize_t i = 0; i < size; i++)
	{
		printf("%02x", (unsigned char)str[i]);
		if (i < size - 1)
			printf(" ");
	}
	printf("\n");
}
