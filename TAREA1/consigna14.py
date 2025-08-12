for i in range(5):
    print(i)  # Imprime del 0 al 4
    
    
for i in range(2, 6):
    print(i)  # Imprime 2, 3, 4, 5
    
    
for i in range(1, 10, 2):
    print(i)  # Imprime 1, 3, 5, 7, 9
    


#Break y else

for i in range(5):
    print(i)
    if i == 3:
        break
else:
    print("El bucle terminó normalmente.")  # Esto no se ejecuta
    
    
    
#While
contador = 0

while contador < 5:
    print(contador)
    contador += 1
    
    
contador = 0

while contador < 5:
    print(contador)
    contador += 1
else:
    print("El bucle terminó sin interrupciones.")
    
    
#Simular Do While en python
while True:
    entrada = input("Escribí 'salir' para terminar: ")
    if entrada == "salir":
        break