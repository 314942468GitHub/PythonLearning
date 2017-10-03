#include <stdio.h>
#include <Python.h>
int add(int x,int y)
{
    printf("add called:  ");
    return (x+y);
}

int minus(int x,int y)
{
    return (x-y);
}

int multiply(int x,int y) 
{
    return (x*y);
}

int divid(int x,int y) 
{
    if (y == 0) 
        return 0;
    else
        return (x/y);
}

static PyObject* cal_add(PyObject* self,PyObject *args)
{
    int res,x,y;
    PyObject * ret;

    res = PyArg_ParseTuple(args,"i",&x);
    if (!res)
        return NULL;
    res = PyArg_ParseTuple(args+1,"i",&y);
    if (!res)
        return NULL;

    res = add(x,y);
    ret = (PyObject*)Py_BuildValue("i",res);
    return ret;
}

static PyObject* cal_minus(PyObject* self,PyObject *args)
{
    int res,x,y;
    PyObject * ret;

    res = PyArg_ParseTuple(args,"i",&x);
    if (!res)
        return NULL;
    res = PyArg_ParseTuple(args+1,"i",&y);
    if (!res)
        return NULL;

    res = minus(x,y);
    ret = (PyObject*)Py_BuildValue("i",res);
    return ret;
}

static PyObject* cal_multiply(PyObject* self,PyObject *args)
{
    int res,x,y;
    PyObject * ret;

    res = PyArg_ParseTuple(args,"i",&x);
    if (!res)
        return NULL;
    res = PyArg_ParseTuple(args+1,"i",&y);
    if (!res)
        return NULL;

    res = multiply(x,y);
    ret = (PyObject*)Py_BuildValue("i",res);
    return ret;
}

static PyObject* cal_divid(PyObject* self,PyObject *args)
{
    int res,x,y;
    PyObject * ret;

    res = PyArg_ParseTuple(args,"i",&x);
    if (!res)
        return NULL;
    res = PyArg_ParseTuple(args+1,"i",&y);
    if (!res)
        return NULL;

    res = divid(x,y);
    ret = (PyObject*)Py_BuildValue("i",res);
    return ret;
}


static PyMethodDef calMethods[] = 
{
    ("add",cal_add,METH_VARARGS),
    ("minus",cal_minus,METH_VARARGS),
    ("multiply",cal_multiply,METH_VARARGS),
    ("divid",cal_divid,METH_VARARGS),
    (NULL,NULL,0),
};