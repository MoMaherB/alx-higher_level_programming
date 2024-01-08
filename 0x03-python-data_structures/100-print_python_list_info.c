#include <Python.h>

/**
 * print_python_list_info - Print info of a Python list.
 * @p: Pointer to a Python list object.
 */
void print_python_list_info(PyObject *p)
{
	int size, mem_allocation, i;
	PyObject *theItem;

	size = PyList_Size(p);
	mem_allocation = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", mem_allocation);

	for (i = 0; i < size; i++)
	{
		theItem = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(theItem)->tp_name);
	}
}
