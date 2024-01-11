#include <Python.h>

void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_list - Print information about Python lists
 * @p: A pointer to the Python list object
 */

void print_python_list(PyObject *p)
{
	const char *t;
	int size, allocation, i;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *variable = (PyVarObject *)p;

	size = variable->ob_size;
	allocation = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocation);

	for (i = 0; i < size; i++)
	{
		t = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, t);
		if (strcmp(t, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - Print information about Python bytes objects
 * @p: A pointer to the Python bytes object
 */

void print_python_bytes(PyObject *p)
{
	unsigned char i, size;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);
	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", size);

	for (i = 0; i < size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}
