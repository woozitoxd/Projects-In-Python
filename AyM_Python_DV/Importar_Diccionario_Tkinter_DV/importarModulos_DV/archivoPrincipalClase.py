from claseAutenticacion import Autenticacion #Acá importamos solo la clase que necesitamos
from claseAutenticacion import * #Acá importamos todo el modulo
#No es recomendable porque puede generar conflictos si hay varias clases o funciones con el mismo nombre
#Es mejor importar solo lo que necesitamos o usar import claseAutenticacion y luego claseAutenticacion.Autenticacion()


def main():

    autenticar = Autenticacion()
    autenticar.login("Elias", "davinci1234")
    
if __name__ == "__main__":
    main()