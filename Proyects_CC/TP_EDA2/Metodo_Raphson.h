#ifndef METODORAPHSON_H
#define METODORAPHSON_H // Defino mi libreria Metodo_Raphson

#include <cmath>
#include <iostream>
#include <tuple>

#include "EcuacionLineal_Raphson.h"

class NewtonRaphson:public SacarRaiz  // Clase NewtonRaphson hereda de Clase Sacar Raiz
{
public:
    void Resultado(); //
    void ingresarValores();
private:
    void setValues(double,double,double);
    void calculo();
    void MostrarTabla();
    double tolerancia;
    double a,b,x1;
    bool converge = true;
    const double intervalos = 6;
    double PuntoInicial();
};


#endif // METODORAPHSON_H
