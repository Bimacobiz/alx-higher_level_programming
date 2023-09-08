/*
 * File: 102-python.c
 */

#include "Python.h"

/**
 * print_python_string - a function that prints information
 *with regards to Python strings.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
	long int string_len;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	string_len = ((PyASCIIObject *)(p))->string_len;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  string_len: %ld\n", string_len);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &string_len));
}
