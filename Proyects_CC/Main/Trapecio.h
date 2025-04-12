#ifndef TRAPECIO_H
#define TRAPECIO_H

#include<iostream>
#include<cmath>
#include <tuple>
#include "AnalisisNumerico.h"

class NewtonCotes : public AnalisisNumerico
{
public:
    void mostrarResultado();
    void ingresarValores();

private:
    int subintervalos;
    double punto_a,punto_b,integral;
    void calculo();
    void setValues(double,double,int);

};

#endif // TRAPECIO_H
