#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - a function that prints information about bytes
 *
 * @p: Python Object
 * Return: nothing
 */
void print_python_bytes(PyObject *p)
{
	char *py_str;
	long int obj_siz, a, extent;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	obj_siz = ((PyVarObject *)(p))->ob_size;
	py_str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", obj_siz);
	printf("  trying string: %s\n", py_str);

	if (obj_siz >= 10)
		extent = 10;
	else
		extent = obj_siz + 1;

	printf("  first %ld bytes:", extent);

	for (a = 0; a < extent; a++)
		if (py_str[a] >= 0)
			printf(" %02x", py_str[a]);
		else
			printf(" %02x", 256 + py_str[a]);

	printf("\n");
}

/**
 * print_python_list - a function that prints information about list
 *
 * @p: Python Object
 * Return: nothing
 */
void print_python_list(PyObject *p)
{
	long int obj_siz, a;
	PyListObject *list;
	PyObject *obj;

	obj_siz = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", obj_siz);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (a = 0; a < obj_siz; a++)
	{
		obj = ((PyListObject *)p)->ob_item[a];
		printf("Element %ld: %s\n", a, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}

