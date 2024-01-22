#include <Python.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <object.h>
/**
 * print_python_list - print python list
 * @p: pointer to PyObject p
 */
void print_python_list(PyObject *p)
{
        size_t a, len, i = 0;
        const char *ch;
        PyListObject *my_list;

        setbuf(stdout, NULL);
        printf("[*] Python list info\n");
        if (PyList_Check(p) == 0)
        {
                printf("  [ERROR] Invalid List Object\n");
                return;
        }
        my_list = (PyListObject *)p;
        len = PyList_GET_SIZE(p);
        a = my_list->allocated;
        printf("[*] Size of the Python List = %ld\n[*] Allocated = %li\n", len, a);
        while (i < len)
        {
                ch = (my_list->ob_item[i])->ob_type->tp_name;
                printf("Element %li: %s\n", i, ch);
                !strcmp(ch, "bytes") ? print_python_bytes(my_list->ob_item[i]) : (void)ch;
                !strcmp(ch, "float") ? print_python_float(my_list->ob_item[i]) : (void)ch;
		i++;
        }
}
/**
 * print_python_bytes - print bytes
 * @p: pointer to PyObject p
 */
void print_python_bytes(PyObject *p)
{
	size_t b, i;
	char *str;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (PyBytes_Check(p) == 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	str = ((PyBytesObject *)(p))->ob_sval, b = PyBytes_Size(p);
	printf("  size: %ld\n  trying string: %s\n", b, str);
	b >= 10 ? b = 10 : b++;
	printf("  first %ld bytes: ", b);
	for (i = 0; i < b - 1; i++)
		printf("%02hhx ", str[i]);
	printf("%02hhx\n", str[i]);
}
/**
 * print_python_float - print python things
 * @p: pointer to PyObject p
 */
void print_python_float(PyObject *p)
{
	char *str;
	double f;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (PyFloat_Check(p) == 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	f = ((PyFloatObject *)(p))->ob_fval;
	str = PyOS_double_to_string(f, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}
