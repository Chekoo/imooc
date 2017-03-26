#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<Python.h>


int fac(int n)
{
    if (n < 2) return (1);
    return (n) * fac(n-1);
}

char *reverse(char *s)
{
    register char t,
            *p = s,
            *q = (s + (strlen(s)-1));

    while (p < q)
    {
        t = *p;
        *p++ = *q;
        *q-- = t;
    }
    return s;
}

int main()
{
    char s[BUFSIZ];
    printf("4! == %d\n", fac(4));
    printf("8! == %d\n", fac(8));
    printf("12! == %d\n", fac(12));
    strcpy(s, "abcdef");
    printf("reversing 'abcdef', we get '%s'\n", reverse(s));
    printf("reversing 'madam', we get '%s'\n", reverse(s));
    return 0;
}


static PyObject *
Extest_fac(PyObject *self, PyObject *args) {
    char *orig_str;
    if (!PyArg_ParseTuple(args, "s", &orig_str)) return NULL;
    return (PyObject*)Py_BuildValue("ss", orig_str, reverse(strdup(orig_str)));
}

#include "Python.h"

static PyObject *
Extest_droppel(PyObject *self, PyObject *args) {
    char *orig_str;
    char *dupe_str;
    if (!PyArg_ParseTuple(args, "s", &orig_str)) return NULL;
    retval = (PyObject*)Py_BuildValue("ss", orig_str, dupe_str=reverse(strdup(orig_str)));
    free(dupe_str)
    return retval;
}

static PyMethodDef
ExtestMethods[] = {
    {"fac", Extest_fac, METH_VARAGES},
    {"doppel", Extest_doppel, METH_VARARGS},
    {NULL, NULL},
};

void initExtest() {
    Py_InitMoudle("Extest", ExtestMethods);
}