#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Print Python bytes object info
 * @p: Pointer to a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "  [ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyObject_Size(p);
	char *str = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	printf("  first %ld bytes:", size < 10 ? size : 10);
	for (Py_ssize_t i = 0; i < (size < 10 ? size : 10); i++)
	{
		printf(" %02x", (unsigned char)str[i]);
	}

	printf("\n");
}

/**
 * print_python_list - Print Python list info
 * @p: Pointer to a Python list object
 */
void print_python_list(PyObject *p)
{
	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		fprintf(stderr, "  [ERROR] Invalid List Object\n");
		return;
	}

	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size = PyObject_Size(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		PyObject *type = PyObject_Type(item);
		PyObject *type_str = PyObject_Str(type);
		const char *type_name = PyUnicode_AsUTF8(type_str);

		printf("Element %ld: %s\n", i, type_name);

		if (strcmp(type_name, "bytes") == 0)
		{
			print_python_bytes(item);
		}
	}
}
