#include <iostream> // Incluyo las librerias para el correcto funcionamiento del programa
#include <cmath>
#include <tuple>


#include "EcuacionLineal_Raphson.h" // Incluyo headers propios.
#include "Metodo_Raphson.h"

void menuOpciones(int opciones, SacarRaiz *analisis);
int menuImprimir();

int main()
{
    SacarRaiz *analisis;
    int accion;
    accion = menuImprimir(); // Variable accion toma el valor retornado por la funcion imprimir.
    while(accion !=2) // Mientras la opcion sea distinta de 2(salir del programa), seguira en el while.
    {
        menuOpciones(accion, analisis);
        accion = menuImprimir();
    }
    return 0;
}

int menuImprimir () // Menu de opciones, retorna entero opcion (valor ingresado por teclado)
{
    int opcion = 0;
    std::cout<<"\t\t\t\t---- Programa para utilizar metodos matematicos ----\n"<<std::endl;
    std::cout<<"1: Usar metodo de Newton Raphson para sacar raiz de una ecuacion no lineal"<<std::endl;
    std::cout<<"2: Para Salir"<<std::endl;
    std::cin>>opcion;
    return opcion;
}


void menuOpciones(int opciones, SacarRaiz *analisis) // Depende cual sea la opcion que ingresó el usuario
{                                                   // Entrara al case segun corresponda.
    switch (opciones)
    {
        case 1:
        {
         std::cout<<"La funcion a utilizar es: x^5+x-2"<<std::endl;
            NewtonRaphson obj; // Instancio objeto a NewtonRaphson
            analisis = &obj;  // Puntero analisis guarda la direcccion donde se encuentra el objeto
            analisis->ingresarValores(); // Analisis apunta al metodo ingresarvalores, al mismo tiempo se invocan los metodos
            analisis->Resultado();  // Analisis apunta al metodo Resultado
        }
        case 2:
        {
            std::cout<<"Saliendo.";
            break;
        }
        default:
        {
            std::cout<<"\nOpcion invalida, Por favor ingrese 1 o 2.\n\n";
            break;
        }
    }
}