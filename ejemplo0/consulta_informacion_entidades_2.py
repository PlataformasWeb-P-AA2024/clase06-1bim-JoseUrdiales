"""
    Consulta de información en las entidades en la base de datos
"""

from base_datos import conn

# se usa el objeto Connection y se accede al método cursor
# para poder realizar las acciones en la base de datos.

cursor = conn.cursor()





# hace consultas a la base de datos
cadena_consulta_sql = "SELECT * from Autor"
cursor.execute(cadena_consulta_sql)
# la información resultante se la obtiene del método fetchall de cursor.
informacion = cursor.fetchall()
print(informacion)
# se realiza un ciclo repetitivo para recorrer la secuencia de información
# resultante
for d in informacion:
    #en la linea 26 se va iterando de dato en dato para no mostrar todo como lo hace la linea 21
    #d es igual a lo que recorra el for y el [0] es la posición que quiero que tome, en este caso la [0]
    #es el nombre y [3] es la edad y le damos formato con %s y %d
    print("EL nombre es %s y la edad es %d " % (d[0], d[3]))
#    print("%s - %s - %s - %d" % (d[0], d[1], d[2], d[3]))

# cerrar el enlace a la base de datos (recomendado)
cursor.close()
