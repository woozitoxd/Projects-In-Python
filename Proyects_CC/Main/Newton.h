#ifndef NEWTONRAPHSON_H
#define NEWTONRAPHSON_H
#include<cmath>
#include<iostream>
#include <tuple>
#include "AnalisisNumerico.h"

class NewtonRaphson : public AnalisisNumerico
{
public:
    void mostrarResultado();
    void ingresarValores();
private:
    double tolerancia;
    double punto_a,punto_b,x1;
    bool converge = true;
    const double INTERVALOS = 9;
    void setValues(double,double,double);
    double definirPuntoInicial();
    void calculo();
    void muestroTabla();
};

#endif // NEWTONRAPHSON_H
