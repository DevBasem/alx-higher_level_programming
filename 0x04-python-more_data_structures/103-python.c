#include <Python.h>

/**
 * print_python_bytes - Print Python bytes object info
 * @p: Pointer to a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size;
	char *trying_str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &trying_str, &size);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", trying_str);
	printf("  first %ld bytes:", size < 10 ? size : 10);
	for (Py_ssize_t i = 0; i < (size < 10 ? size : 10); i++)
	{
		printf(" %02x", (unsigned char)trying_str[i]);
	}
	printf("\n");
}

/**
 * print_python_list - Print Python list info
 * @p: Pointer to a Python list object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	PyListObject *list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = list->ob_item[i];
		PyTypeObject *type = Py_TYPE(item);
		printf("Element %ld: %s\n", i, type->tp_name);
		if (PyBytes_Check(item))
		{
			print_python_bytes(item);
		}
	}
}
