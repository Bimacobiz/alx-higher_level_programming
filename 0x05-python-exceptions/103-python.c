/*
 * File: 103-python.c
 * Auth: Collins Mahigi
 */
#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - prints important information about Python lists.
 * @p: An object in the PyObject list.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t dimension, allocated_items, k;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	dimension = var->ob_size;
	allocated_items = list->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", dimension);
	printf("[*] Allocated = %ld\n", allocated_items);

	for (k = 0; k < dimension; k++)
	{
		type = list->ob_item[k]->ob_type->tp_name;
		printf("Element %ld: %s\n", k, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[k]);
		else if (strcmp(type, "float") == 0)
			print_python_float(list->ob_item[k]);
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t dimension, k;
	PyBytesObject *bytes = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  dimension: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
		dimension = 10;
	else
		dimension = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %ld bytes: ", dimension);
	for (k = 0; k < size; k++)
	{
		printf("%02hhx", bytes->ob_sval[k]);
		if (k == (dimension - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - Prints basic info about Python float objects.
 * @p: A PyObject float object.
 */
void print_python_float(PyObject *p)
{
	char *data_buffer = NULL;

	PyFloatObject *float_obj = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	data_buffer = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", data_buffer);
	PyMem_Free(data_buffer);
}

