#include "Metodo_Raphson.h"

void NewtonRaphson::ingresarValores()
{
    double a,b,aux_tolerancia;

    std::cout <<"Calcular la raiz dentro del intervalo en los puntos: [a,b]"<<std::endl;
    std::cout<<"Ingrese el intervalo inicial\n"<<std::endl;
    std::cout << "\nPunto inicial [a]: ";
    std::cin >> a;  // Se pide el ingreso del punto inicial, se guarda en la variable A
    std::cout << "Punto final [b]: ";
    std::cin >> b; // Se pide el ingreso del punto final, se guarda en la variable B
    std::cout << "Ingrese la tolerancia: "<<std::endl;
    std::cin >> aux_tolerancia; // Se pide el ingreso de la tolerancia, se guarda en la variable auxiliar tolerancia.

    this->setValues(a,b,aux_tolerancia);
}


void NewtonRaphson::MostrarTabla()
{
    int puntos = intervalos + 1;
    double ancho = (a - b)/ intervalos; // El ancho guarda el resultado de la resta entre punto inicial y final, sobre intervalos

    std::cout << "\n\tx\t\tf(x) " << std::endl;
    for(int i = 0; i<puntos; i++)
    {
        std::cout << "\t"<<a<<"\t\t"<<this->f(a)<<std::endl;
        a = a + ancho;
    }
}

double NewtonRaphson::PuntoInicial()
{
    double x0;
    std::cout << "Defina un punto inicial: "<<std::endl;
    std::cin >> x0;
    return x0;
}

void NewtonRaphson::calculo()
{
    int iteraciones=0;
    double x0, error;
    x0 = this->PuntoInicial();

    std::cout << "Aproximacion inicial: "<<"\n";
    std::cout << "x0 = "<< x0 <<"\n"<<"f(x0) = " << this->f(x0)<<"\n"<<"f'(x0) = "<<this->df(x0) << std::endl;
    iteraciones++;

    do
    {
        if(iteraciones > 100) // Se le asigna un limite de iteraciones.
        {
            converge = false;
            break;
        }
        else
        {
            x1 = x0 -this->f(x0)/this->df(x0);
                                    // Se calcula el error
            error = fabs(x1 - x0);
                                // Se muestran por pantalla todas las iteraciones
            std::cout << "\nIteracion #" << iteraciones<<std::endl;
            std::cout<<"x"<< iteraciones << " = "<<x1<<"\n"
                     <<"f(x"<<iteraciones<<") = "<< this->f(x1)<<"\n"
                     <<"f'(x"<<iteraciones<<") = "<< this->df(x1)<<"\n"
                     <<"error = "<< error<<std::endl;
            // Si tenemos un error menor a la tolerancia, el programa se termina.
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

void NewtonRaphson::Resultado()
{
    this->MostrarTabla();
    this->calculo();
    if(converge)
        std::cout<<"\nPara una tolerancia de "<<tolerancia<<" la raiz de la funcion es: "<< x1 << std::endl << std::endl;
    else
        std::cout << "\n\nSe sobrepaso la maxima cantidad de iteraciones permitidas."<<std::endl;
}

void NewtonRaphson::setValues(double c,double d,double aux_tolerancia) // Constructor
{
    a = c;
    b = d;
    tolerancia = aux_tolerancia;
}