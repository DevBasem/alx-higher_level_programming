#include <stdio.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

/**
 * print_python_list - Print Python list info
 * @p: Pointer to a Python list object
 */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid List Object\n");
		return;
	}

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
	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytesObject *bytes = (PyBytesObject *)p;
	Py_ssize_t size = ((PyVarObject *)p)->ob_size;
	char *str = bytes->ob_sval;

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	printf("  first 10 bytes: ");
	Py_ssize_t max_bytes = size < 10 ? size : 10;
	for (Py_ssize_t i = 0; i < max_bytes; i++)
	{
		printf("%02x", (unsigned char)str[i]);
		if (i < max_bytes - 1)
			printf(" ");
	}
	printf("\n");
}
