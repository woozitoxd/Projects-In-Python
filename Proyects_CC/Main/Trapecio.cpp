#include "Trapecio.h"

void NewtonCotes::calculo()
{
    int intervalo, punto_x_actual;
    double ancho_intervalos ,suma=0;
    double puntos_en_x[subintervalos+1],puntos_en_y[subintervalos+1];
    ancho_intervalos =(punto_b - punto_a)/subintervalos;
    for (intervalo=0; intervalo<=subintervalos; intervalo++)
    {
        //se evalúa x0,...xn e y0,...yn
        puntos_en_x[intervalo]=punto_a+intervalo*ancho_intervalos;
        puntos_en_y[intervalo]=this->f(puntos_en_x[intervalo]);
    }
    for (intervalo=1; intervalo<subintervalos; intervalo++)          //se evalúa sin los extremos ancho*(y1+...+yn-1)
    {
        suma=suma+ancho_intervalos *puntos_en_y[intervalo];
    }
    this->integral=ancho_intervalos/2.0*(puntos_en_y[0]+puntos_en_y[subintervalos])+suma;        //ancho/2*[y0+yfinal+2(y1+y2+y3+...yn-1)]
}

void NewtonCotes::mostrarResultado()
{
    this->calculo();
    std::cout<<std::endl<<"La integral definida es "<<this->integral<<std::endl<<std::endl;
}

void NewtonCotes::ingresarValores()
{
    double a,b;
    int n;
    std::cout<<"Ingrese los limites de la integración"<<std::endl;
    std::cout<<"Limite inicial: ";
    std::cin>>a;
    std::cout<<"Limite final: ";
    std::cin>>b;
    std::cout<<"Ingrese el número de subintervalos: ";
    std::cin>>n;

    this->setValues(a,b,n);
}
void NewtonCotes::setValues(double a,double b,int n)
{
    this->punto_a = a;
    this->punto_b = b;
    this->subintervalos = n;
}
