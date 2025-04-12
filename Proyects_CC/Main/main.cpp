#include<iostream>
#include<cmath>
#include <tuple>

#include "Newton.h"
#include "Trapecio.h"
#include "AnalisisNumerico.h"

void menuLlamaAccion(int opciones, AnalisisNumerico *analisis);
int menuImprimir();

int main()
{
    AnalisisNumerico *analisis;
    int cantRegistrada;
    int accion;
    accion = menuImprimir();
    while(accion !=3)
    {
        std::cout<<"La función a utilizar es: 16x^3-12x^2"<<std::endl;
        menuLlamaAccion(accion, analisis);
        accion = menuImprimir();
    }
    return 0;
}

void menuLlamaAccion(int opciones, AnalisisNumerico *analisis)
{
    switch (opciones)
    {
        case 1:
        {

            // 0.5, 1, 0.00001, 0.7 = 0.75
            NewtonRaphson obj;
            analisis = &obj;
            analisis->ingresarValores();
            analisis->mostrarResultado();
            break;
        }
        case 2:
        {

            // 3, 7, 99 = 8016.25
            NewtonCotes obj;
            analisis = &obj;
            analisis->ingresarValores();
            analisis->mostrarResultado();
            break;
        }
        case 3:
        {
            std::cout<<"Saliendo";
            break;
        }
        default:
        {
            std::cout<<"Opcion no valida, ingrese una correcta";
            break;
        }
    }
}

int menuImprimir ()
{
    int opcion = 0;
    std::cout<<"Ingrese por teclado la opcion que quiere tomar:"<<std::endl;
    std::cout<<"1: Usar metodo de Newton Raphson para obtener raíz de la funcón"<<std::endl;
    std::cout<<"2: Usar un metodo de Newton Cotes para obtener integral"<<std::endl;
    std::cout<<"3: Para Salir"<<std::endl;
    std::cin>>opcion;
    return opcion;
}
