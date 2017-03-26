#include<stdio.h>
#include<stdlib.h>
#include<string.h>

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


/*包装函数*/
static PyObject *
Extest_fac(PyObject *self, PyObject *args) {
    char *orig_str;
    /*解析python传过来的数据，使用格式字符串"i"，表示期望得到一个整型的变量，保存到num变量中*/
    if (!PyArg_ParseTuple(args, "s", &orig_str)) return NULL;
    return (PyObject*)Py_BuildValue("ss", orig_str, reverse(strdup(orig_str))); /*将结果转为python的整形类型并返回*/
}


static PyObject *
Extest_droppel(PyObject *self, PyObject *args) {
    char *orig_str;    /*原始字符串*/
    char *dupe_str;    /*反转后的字符串*/
    /*解析python传过来的数据，使用格式字符串"i"，表示期望得到一个整型的变量，保存到num变量中*/
    if (!PyArg_ParseTuple(args, "s", &orig_str)) return NULL;
    /*将结果转为python的整形类型并返回*/
    retval = (PyObject*)Py_BuildValue("ss", orig_str, dupe_str=reverse(strdup(orig_str)));
    free(dupe_str)  /*释放这个字符串*/
    return retval;
}

static PyMethodDef
ExTtestMethods[] = {  /*METH_VARARGS表示参数以元组形式传入*/
    {"fac", Extest_fac, METH_VARAGES},
    {"doppel", Extest_doppel, METH_VARARGS},
    {NULL, NULL},  /*放一个null数组表示列表的结束*/
};

void initExtest() {
    Py_InitMoudle("Extest", ExtestMethods);
}