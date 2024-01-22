#include <Python.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <object.h>

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

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
	size_t len, i = 0;
	char *s;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (PyBytes_Check(p) == 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	s = ((PyBytesObject *)(p))->ob_sval;
       	len = PyBytes_Size(p);
	printf("  size: %ld\n  trying string: %s\n", len, s);
	if (len >= 10)
		len = 10;
	else
		len++;
	printf("  first %ld bytes: ", len);
	while (i < len - 1)
	{
		printf("%02hhx ", s[i]);
		i++;
	}
	printf("%02hhx\n", s[i]);
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
