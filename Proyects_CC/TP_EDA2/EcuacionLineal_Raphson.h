#ifndef ECUACIONLINEAL_H
#define ECUACIONLINEAL_H

#include <cmath>

class SacarRaiz // La clase mas importante de todas, con esta voy a mostrar los resultados por pantalla y setear los valores
{               // Al mismo tiempo, de esta se heredaran los metodos
    public:
        virtual void Resultado()=0; //
        virtual void ingresarValores()=0;
    private:
        virtual void calculo()=0; //
    protected:
        double f(double x); //
        double df(double x);
};

#endif // ECUACIONLINEAL_H
