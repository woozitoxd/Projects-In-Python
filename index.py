import requests
from pymongo import MongoClient
import pprint
import json
import datetime

def ObtenerDatosProvincias():
    provincias_url = 'https://apis.datos.gob.ar/georef/api/provincias'
    provincias_response = requests.get(provincias_url)
    provincias_data = provincias_response.json()
    return provincias_data['provincias']  #Una vez que obtuve los datos de la api, retorno como array de provincias

###############################################################################

def GuardarProvincias(provincias_collection, provincias):
    provincias_collection.insert_many(provincias) #inserto los datos que recibi de la funcion en la coleccion provincias

###############################################################################
# funcion para obtener y guardar localidades de una provincia en la base de datos

def ObtenerLocalidades(provincia, localidades_collection, log_file):
    provincia_id = provincia['id']
    localidades_url = f'https://apis.datos.gob.ar/georef/api/municipios?provincia={provincia_id}'
    localidades_response = requests.get(localidades_url)
    localidades_data = localidades_response.json()
    localidades = localidades_data['municipios']

    if localidades:
        localidades_collection.insert_many(localidades) #Aca guardo los datos que obtuve en la coleccion localidades
        log_file.write(f'{datetime.datetime.now()}: Localidades de {provincia["nombre"]} insertadas en la base de datos\n')#Registro la actividad en el archivo
    else:
        print(f'No hay localidades para la provincia {provincia["nombre"]}')
        log_file.write(f'{datetime.datetime.now()}: No hay localidades para la provincia {provincia["nombre"]}\n')

###############################################################################
# funcion para obtener el clima de cada localidad y guardarlo en la base de datos

def ObtenerClimas(localidades_collection, clima_collection, api_key, log_file):
    for localidad in localidades_collection.find():
        ciudad = localidad['nombre']
        provincia = localidad['provincia']['nombre']

        try:
            clima_url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad},{provincia}&appid={api_key}' #Api donde obtengo los datos del clima
            clima_response = requests.get(clima_url)
            clima_data = json.loads(clima_response.text)

            if 'cod' in clima_data and clima_data['cod'] == '404': #Manejo en caso de error
                print(f'No se encontraron datos de clima para {ciudad}, {provincia}')
                log_file.write(f'{datetime.datetime.now()}: No se encontraron datos de clima para {ciudad}, {provincia}\n')
            else:
                clima_collection.insert_one({# aca guardo los datos en la coleccion 'clima'
                    'ciudad': ciudad,
                    'provincia': provincia,
                    'clima': clima_data
                })
                log_file.write(f'{datetime.datetime.now()}: Clima de {ciudad}, {provincia} insertado en la base de datos\n') #Guardo en el registro txt

        except requests.exceptions.RequestException as e:
            print(f'Error al obtener el clima para {ciudad}, {provincia}: {e}')
            log_file.write(f'{datetime.datetime.now()}: Error al obtener el clima para {ciudad}, {provincia}: {e}\n')

###############################################################################

def ConsultarProvincia(provincias_collection, provincia_query):
    result = provincias_collection.find_one({'nombre': provincia_query}) #Consulta del nombre de una provincia
    if result:
        print(f'Provincia: {result["nombre"]}')
    else:
        print(f'No se encontró la provincia {provincia_query}')

###############################################################################

def ConsultarLocalidad(localidades_collection, localidad_query, log_file):
    localidad_result = localidades_collection.find_one({'nombre': localidad_query}) #Consulta del nombre de una localidad
    if localidad_result:
        print(f'Localidad: {localidad_result["nombre"]}') #Muestro en la terminal los resultados que obtuve
        log_file.write(f'{datetime.datetime.now()}: Se realizó una consulta de localidad {localidad_result["nombre"]}\n') #Lo guardo en el registro txt
    else:
        print(f'No se encontró la localidad {localidad_query}')
        log_file.write(f'{datetime.datetime.now()}: No se encontraron datos en la consulta de localidad {localidad_result["nombre"]}\n')

###############################################################################

def main():
    client = MongoClient('mongodb://localhost:27017') 
    db = client['argentina'] #Creo la base
    provincias_collection = db['provincias']  #Creo las colecciones para la base
    localidades_collection = db['localidades']
    clima_collection = db['clima']
    log_file = open('registro_actividades.txt', 'a') #Creo el archivo donde llevare registro de las actividades del programa

    provincias = ObtenerDatosProvincias() #Provincias tiene el valor que retorne de la funcion, en este caso, las provincias que obtuve de la api
    GuardarProvincias(provincias_collection, provincias) #Le paso como parametro a la funcion que guarda la provincia la creacion d la coleccion y la variable provincias

    for provincia in provincias:
        ObtenerLocalidades(provincia, localidades_collection, log_file)

    api_key = ''  #mi clave de la API para obtener el clima
    ObtenerClimas(localidades_collection, clima_collection, api_key, log_file)

    # Realizar consultas en la base de datos
    ConsultarProvincia(provincias_collection, 'Buenos Aires')
    ConsultarLocalidad(localidades_collection, 'Apóstoles', log_file)

    client.close() #Cierro la conexion a la bbdd
    log_file.close() #Cierro el archivo de registro de acividades

if __name__ == "__main__":
    main()