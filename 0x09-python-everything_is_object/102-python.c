#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_string - Prints information about Python strings
 * @p: Pointer to a Python object
 */
void print_python_string(PyObject *p)
{
    printf("[.] string object info\n");

    if (PyUnicode_Check(p))
    {
        PyUnicodeObject *unicode = (PyUnicodeObject *)p;

        printf("  type: %s\n", PyUnicode_IS_COMPACT_ASCII(unicode) ? "compact ascii" : "compact unicode object");
        printf("  length: %ld\n", PyUnicode_GET_LENGTH(unicode));
        printf("  value: %s\n", PyUnicode_AsUTF8(unicode));
    }
    else
    {
        printf("  [ERROR] Invalid String Object\n");
    }
}
