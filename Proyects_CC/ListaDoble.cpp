#include <iostream>
#include "Lista.h"
#include "Nodo.h"

using namespace std;

#define MENU cout<<endl<<"1 - Ingresa Datos"<<endl<<"


int main(void)
{
    Lista Elementos;
    int Opcion, Dato;
    do{
        MENU;
        cin>>Opcion;
        switch(Opcion){
    case 1:
        Elementos.Insertar();
        break;
    case 2:
        Elementos.LeeLista();
        break;
    case 3:
        cout<<endl<<"Ingrese el dato a borrar: ";
        cin>>Dato;
        Elementos.Borra(Dato);
        break;
        }
    }
    while(Opcion!=4);
    return 0;
}
