#include "Nodo.h"
#include <iostream>

using namespace std;

Nodo::Nodo()
{
    cout<<endl<<"Ingrese el dato: ";
    cin>>Dato;
    Siguiente = NULL;
    Anterior = NULL;

}
bool Nodo::operator >(Nodo X)
{
    if(Dato >X.Dato)
        return
}
