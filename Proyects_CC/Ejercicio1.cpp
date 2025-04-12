#include <iostream>

using namespace std;

// Declarar clases publicas y una protegida para la demostracion de error para compilar.

class objeto
{
    public:
        int a;
        int x;
    public:
        float b;
    protected:
        float c;
};

int main()
{
    cout<<"HOLA MUNDO!!";
    objeto o;
    o.x = 5;
    o.a = 'A';
    o.b = 3.5;
   // o.c = 2.5; // La clase esta protegida, entonces no se puede utilizar.

    cout<<"\n"<<o.a<<"\n";
    cout<<o.b<<"\n";
    cout<<o.x;

}

