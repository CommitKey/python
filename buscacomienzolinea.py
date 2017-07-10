# (c) Manuel Galeote 2017
# Extract data from a log

nombre = input('Nombre del fichero origen: ')
nombredestino = input('Nombre del fichero destino: ')
dato = input('Dato a buscar: ')
try:
    fichero = open(nombre)
except:
    print('Error al abrir el fichero origen.')
    exit()
try:
    ficherodestino = open(nombredestino, 'w')
except:
    print('Error al crear el fichero destino.')
    exit()
for linea in fichero:
    #linea = linea.rstrip()
    if linea.startswith(dato):
        print(linea)
        ficherodestino.write(linea+'\n')
fichero.close()
ficherodestino.close()
