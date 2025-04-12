import time
import logging #Importamos modulo de logueo
from concurrent.futures import ThreadPoolExecutor

#ThreadPoolExecutor se encarga degestionar un conjunto de hilos.

logging.basicConfig(level=logging.DEBUG,
                    format='%(thread)d - %(threadName)s: %(message)s')
#informa en pantalla cuando estemos depurando

def un_metodo_que_suma(par1, par2):
    time.sleep(2)
    
    logging.info(f'La suma de {par1} + {par2} es: {par1+par2}\n')
    
def un_metodo_que_resta(par1, par2):
    time.sleep(1)
    
    logging.info(f'La resta de {par1} - {par2} es: {par1 - par2}\n')

if __name__ == '__main__':
    
    #ejecutor = ThreadPoolExecutor(max_workers=2)
    #con el metodo submit, agregamos hilos/tareas al ejecutor/gestor de hilos

    with ThreadPoolExecutor(max_workers=2) as ejecutor:
    #para evitar que el gestor de hilos viva durante la ejecucion de los hilos, usamos with
    #esto sirve para ahorrar tiempo en memoria ya que tenemos definido el conjunto de tareas a ejecutar
        ejecutor.submit(un_metodo_que_suma, 10,20) #Al gestor/ejecutor, le indicamos el metodo a ejecutar y los parametros a utilizar por el metodo
        ejecutor.submit(un_metodo_que_resta, 20, 10)
        
        ejecutor.submit(un_metodo_que_suma, 10,80) #Al gestor/ejecutor, le indicamos el metodo a ejecutar y los parametros a utilizar por el metodo
        ejecutor.submit(un_metodo_que_resta, 20, 90)
        
        ejecutor.submit(un_metodo_que_suma, 10,30) #Al gestor/ejecutor, le indicamos el metodo a ejecutar y los parametros a utilizar por el metodo
        ejecutor.submit(un_metodo_que_resta, 20, 80)

        ejecutor.submit(un_metodo_que_suma, 10,20) #Al gestor/ejecutor, le indicamos el metodo a ejecutar y los parametros a utilizar por el metodo
        ejecutor.submit(un_metodo_que_resta, 20, 150)
        
        ejecutor.submit(un_metodo_que_suma, 20,20) #Al gestor/ejecutor, le indicamos el metodo a ejecutar y los parametros a utilizar por el metodo
        ejecutor.submit(un_metodo_que_resta, 170, 350)
        
    ##instruccion 1
    
    ##tarea A
    
    ##tarea B
    
    
    
    #Ultima tarea