# (c) Manuel Galeote 2017
# Extract data from a table->db->mysql
import pymysql.cursors
import getpass
ghost = input('Host: ')
guser = input('Usuario: ')
gpassword = getpass.getpass('Password: ')
gdb = input('Nombre de la base de datos: ')
gtabla = input('Nombre de la tabla: ')
gficherodestino = input('Nombre del fichero: ')

connection = pymysql.connect(host=ghost,
                             user=guser,
                             password=gpassword,
                             db=gdb,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
try:
    fichero = open(gficherodestino,'w')
except:
    print('Se ha producido un error al abrir el fichero destino.')
try:
    cursor = connection.cursor()
    sql = "SELECT * FROM "+gtabla
    cursor.execute(sql)
    result = cursor.fetchall()
    for linea in result:
        # claves = linea.keys()
        # for item in claves:
        #     print(item + ' = ' + str(linea[item]))
        for elemento in linea:
            try:
                fichero.write(elemento + ' = ' + str(linea[elemento])+'\n')
            except:
                print('Se ha producido un error al guardar el fichero destino')
            print(elemento + ' = ' + str(linea[elemento]) )
except:
    print('Se ha producido un error al tratar con la base de datos.')
finally:
    fichero.close()
    connection.close()
