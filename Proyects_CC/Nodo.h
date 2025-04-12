#ifndef NODO_H
#define NODO_H

struct Nodo
{
int Dato;
Nodo *Siguiente, *Anterior;
Nodo();
bool operator >(Nodo);
};

#endif // NODO_h
