#include <Python.h>

/**
 * print_python_list_info - prints important information about lists
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int size, allocation, i;
	PyObject *obj;

	size = Py_SIZE(p);
	allocation = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocation);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
