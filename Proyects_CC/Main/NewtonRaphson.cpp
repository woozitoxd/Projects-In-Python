#include "NewtonRaphson.h"

void NewtonRaphson::muestroTabla()
{
    int puntos = INTERVALOS + 1;
    double ancho = (punto_b-punto_a)/INTERVALOS;

    std::cout << "\n\tx\t\tf(x) " << std::endl;
    for(int i = 0; i<puntos; i++)
    {
        std::cout << "\t"<<punto_a<<"\t\t"<<this->f(punto_a)<<std::endl;
        punto_a = punto_a + ancho;
    }
}

double NewtonRaphson::definirPuntoInicial(){
    double x0;
    std::cout << "Defina un punto inicial: "<<std::endl;
    std::cin >> x0;
    return x0;
}

void NewtonRaphson::calculo()
{
    int iteraciones=0;
    double x0, error;
    x0 = this->definirPuntoInicial();

    std::cout << "Aproximación inicial: "<<"\n";
    std::cout << "x0 = "<< x0 <<"\n"<<"f(x0) = " << this->f(x0)<<"\n"<<"f'(x0) = "<<this->df(x0) << std::endl;
    iteraciones++;

    do
    {
        if(iteraciones > 150)
        {
            converge = false;
            break;
        }
        else
        {
            x1 = x0 -this->f(x0)/this->df(x0);
            //Calculo del error
            error = fabs(x1 - x0);
            //muestro todas las iteraciones
            std::cout << "\nIteracion #" << iteraciones<<std::endl;
            std::cout<<"x"<< iteraciones << " = "<<x1<<"\n"
                     <<"f(x"<<iteraciones<<") = "<< this->f(x1)<<"\n"
                     <<"f'(x"<<iteraciones<<") = "<< this->df(x1)<<"\n"
                     <<"error = "<< error<<std::endl;
            //si el error es menor a la tolerancia se termina el programa
            if(error <= tolerancia)
            {
                converge = true;
                break;
            }
            else
            {
                x0 = x1;
                iteraciones++;
            }
        }
    }
    while(1);
}

void NewtonRaphson::mostrarResultado()
{
    this->muestroTabla();
    this->calculo();
    if(converge)
        std::cout<<"\nPara una tolerancia de "<<tolerancia<<" la raíz de f es: "<< x1 << std::endl << std::endl;
    else
        std::cout << "\n\nSe sobrepaso la máxima cantidad de iteraciones permitidas."<<std::endl;
}

void NewtonRaphson::setValues(double a,double b,double aux_tolerancia)
{
    punto_a = a;
    punto_b = b;
    tolerancia = aux_tolerancia;
}
void NewtonRaphson::ingresarValores()
{
    std::cout << "Este programa calcula la raiz dentro del intervalo [a,b]"<<std::endl;
    std::cout<<"Ingrese el intervalo inicial [a,b]"<<std::endl;
    double a,b,aux_tolerancia;
    std::cout << "\nLimite inicial: ";
    std::cin >> a;
    std::cout << "Limite final: ";
    std::cin >> b;
    std::cout << "Ingrese la tolerancia: "<<std::endl;
    std::cin >> aux_tolerancia;
    this->setValues(a,b,aux_tolerancia);
}
