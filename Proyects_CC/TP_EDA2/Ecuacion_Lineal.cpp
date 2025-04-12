#include "EcuacionLineal_Raphson.h" // Incluimos nuestro header de ecuacion lineal

double SacarRaiz::f(double x)
{
    return x*x*x*x*x+x-2; // Funcion a utilizar
}

double SacarRaiz::df(double x)
{
    return 5*x*x*x*x+1;  // Funcion derivada
}

