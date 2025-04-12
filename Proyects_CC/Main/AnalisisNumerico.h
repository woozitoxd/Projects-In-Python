#ifndef ANALISISNUMERICO_H
#define ANALISISNUMERICO_H

#include<cmath>

class AnalisisNumerico
{
    public:
        virtual void mostrarResultado()=0;
        virtual void ingresarValores()=0;
    private:
        virtual void calculo()=0;
    protected:
        double f(double x);
        double df(double x);
};

#endif // ANALISISNUMERICO_H
