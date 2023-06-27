import numpy
import os
import msvcrt




lista_ruts = []
lista_nombre = []
lista_mascota = []
lista_cantidad_de_dias = []
def validar_opcion():
    while True:
        try:
            opc = int(input("Ingrese opción: "))
            if opc in(1,2,3,4):
                return opc
            else:
                print("ERROR! OPCIÓN INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
            
            
                      
def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut(sin puntos ni dígito verificador): "))
            if len(str(rut)) >= 7 and len(str(rut)) <= 8:
                return rut
            else:
                print("ERROR! EL RUT DEBE TENER ENTRE 7 y 8!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")     
    
    
def validar_nombre():
    while True:
        nombre = input("Ingrese nombre: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")
            

def validar_nombre_mascota():
    while True:
        mascota = input("Ingrese nombre de la mascota: ")
        if len(mascota.strip()) >= 3 and mascota.isalpha():
            return mascota
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")
            
def identificador_unico():
 contador + 1
 print(contador)
 
 
             
def cantidad_de_dias():
    while True:
        try:
            cantidad_dias = int(input("ingrese la cantidad de dias que se quedara su mascota"))
            if cantidad_dias >= 1:
             return cantidad_dias
            else:
               print("debe ingresar un numero mayor a 0")
        except:
               print("ERROR DEBE INGRESAR UN NUMERO ENTERO:") 
    

            
def validar_habitacion():
    while True:
        try:
            habitacion = int(input("Ingrese opción: "))
            if habitacion > 1 and habitacion < 10:
                return habitacion
            else:
                print("ERROR! OPCIÓN INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
            
def grabar():
     rut = validar_rut()
     lista_ruts.append(rut)
     nombre = validar_nombre()
     lista_nombre.append(nombre)
     nombre_de_macosta = validar_nombre_mascota()
     lista_mascota.append(nombre_de_macosta)
     identificador_unico = 0
     identificador_unico += 1
     cantidad_de_dias = cantidad_de_dias()
     lista_cantidad_de_dias.append(cantidad_de_dias)
     validar_habitacion = validar_habitacion()
 
    
def buscar_mascota():
    validar_rut()
    if validar_rut() not in lista_ruts:
        return validar_rut
    else:
     print("usted no esta tiene su mascota")
 


            




while True:
    print(""" MOSTRAR MENU
     1.GRABAR
     2.BUSCAR
     3.RETIRARSE
     4.SALIR  
        """)
    opcion = validar_opcion()
    if opcion == 1:
      grabar()
    elif opcion == 2:
        validar_rut
    elif opcion == 3:
        pass
    else:
        print("Salir")
