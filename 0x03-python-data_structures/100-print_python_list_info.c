#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *py_list)
{
    long int list_size = PyList_Size(py_list);
    int idx;
    PyListObject *list_obj = (PyListObject *)py_list;

    printf("[*] Size of the Python List = %li\n", list_size);
    printf("[*] Allocated = %li\n", list_obj->allocated);
    for (idx = 0; idx < list_size; idx++)
        printf("Element %i: %s\n", idx, Py_TYPE(list_obj->ob_item[idx])->tp_name);
}
