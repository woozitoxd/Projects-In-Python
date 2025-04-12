#include "AnalisisNumerico.h"

double AnalisisNumerico::f(double x)
{
    return 16*x*x*x-12*x*x;
}

double AnalisisNumerico::df(double x)
{
    return 48*x*x-24*x;
}
