#Programa: CRUD con operaciones básicas de la BDD
#Autor: Lucio David Morán Brizuela
#Fecha: 16 de Julio 2019
#Materia: Lenguajes y Autómatas II

#------------------------------------------------------
#----------------------CREATE--------------------------
#Primer paso: Abrir la conexión a la base de datos
import pymysql

try:
    #Cadena de conexión al servidor de BDD
    db = pymysql.connect("localhost","root","","automatas2")
    print("Conexión establecida...")
except:
    print("ERROR: Falló la conexión...")



#READ
def mostrar(*args):
    try:
        db = pymysql.connect(host='localhost', user='root', password='',db='automatas2')
        print("Conexión ESTABLECIDA...")
        try:
            with db.cursor() as cursor:
                cursor.execute("SELECT clave, nombre FROM keyword;")
                keyword = cursor.fetchall()

        finally:
            db.close()

    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("ERROR: No se pudo realizar la conexión", e)



#UPDATE
def mod(*args):
    try:
        db = pymysql.connect(host='localhost', user='root', password='',db='automatas2')
        print("Conexión ESTABLECIDA...")
        try:
            with db.cursor() as cursor:
                mod = ("UPDATE keyword SET nombre='' WHERE clave= ;")
                newVersion = "" 
                edit = 2
                cursor.execute(mod, (newVersion, edit))
                #Commit para realizar los cambios
                db.commit()
        finally:
            db.close() 

    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("ERROR: No se pudo realizar la conexión", e)



#DELETE
def borrar(*args):
    try:
        db = pymysql.connect(host='localhost', user='root', password='',db='automatas2')
        print("Conexión ESTABLECIDA...")
        try:
            with db.cursor() as cursor:
                delet = ("DELETE from keyword WHERE clave= ;")
                cursor.execute(delet)
                #Commit para realizar los cambios
                db.commit()
        finally:
            db.close() 

    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("ERROR: No se pudo realizar la conexión", e)


def mostrarPDF(*args):
    ml = 18
    t = ""
    j = 748

    c = canvas.Canvas('Reporte.pdf')

    c.drawString(ml, 830, "Empresa - 'La Gran Empresa' ")
    c.drawString(ml, 810, "Reporte generado en la fecha: "+time.strftime("%d/%m/%y"))
    c.drawString(ml, 760, "Clave: "+t+" Nombre: ")

    cursor = db.cursor()
    mostrar = "SELECT * from keyword;"
    cursor.execute(mostrar)
    result = cursor.fetchall()

    for row in result:
        clave = row[0]
        nombre = row[1]
        c.drawString(ml, j, "   {0}".format(clave, nombre)+ t +"    {1}".format(clave, nombre))
        j = j - 15
    c.save()
    

def main():
    ciclo = True
    while (ciclo == True):
        print("---CRUD de una Base de Datos---")
        print("1. Mostrar los datos de la BDD")
        print("2. Modificar un elemento de la BDD")
        print("3. Eliminar un elementos de la BDD")
        print("4. Mostrar y generar PDF")
        print("5. SALIR")
        opcion= int(input("ELIJA UNA OPCION: "))
        
        print("\n")
        
        if(opcion == 1):
            mostrar()
        elif (opcion == 2):
            mod()
        elif (opcion == 3):
            borrar()
        elif (opcion == 4):
            mostrarPDF()
        elif (opcion == 5):
            print("...FIN DEL PROGRAMA...")
            ciclo = False
        else:
            print("Selecciona un entero entre 1 y 5")
            print("\n")


if __name__ == "__main__":
    main()
