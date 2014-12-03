
#***************************Librerias***************************
import time

#****************************Funciones**************************
def mostrarinventario():#muestra inventario
    for x in inventario:
        for y,z in inventario[x].items():
            print "\n-Producto: "+str(x)
            print "Precio sin IVA: Q"+str(y)+". IVAQ"+str(z)+". Total:",(int(y)+int(z)),"\n"


def nuevafactura():#vacia factura para nuevo cliente
    for i in factura:
        factura.remove(i)

def compnum(numero): #funcion para comprobar que se ingrese un numero real valido
    try:#comprueba si es real
        numero = float(numero)
        numerovalido = "Float"
        if numero%1==0:
            numerovalido="Int"
        if numero<=0:
            return "Invalido"
        return numerovalido
    except ValueError:
        numerovalido = "Invalido"
        return numerovalido

def compresp(respuesta): #comprueba si lo ingresado son letras
    respuesta = respuesta.lower()
    if respuesta.isalpha()==True:
        if respuesta=="si":
            respuestavalida = True
        elif respuesta == "no":
            respuestavalida = True
        else:
            respuestavalida = False
    else:
        respuestavalida = False
    return respuestavalida 
    
def menu():
    opcion = False
    while(opcion==False):
        print "1. Ingreso"
        print "2. Compra"
        print "3. Mostrar inventario"
        print "4. Salir"
        opcionmenu = raw_input("Ingrese opcion(1-3): ")
        if compnum(opcionmenu)!="Invalido":
            if opcionmenu == "1" or opcionmenu=="2" or opcionmenu=="3"or opcionmenu=="4":
                opcion = True
            else:           
                opcion = False
                print "Opcion invalida, solo se permite (1-3)"
        else:
            opcion = False
    return opcionmenu

def compra():#funcion que pregunta que membresia tiene
    fincompra = False
    total = 0
#    descuento = membresia()
    print "\nCargando inventario... Porfavor espere..."
    time.sleep(1) 
    mostrarinventario()
    time.sleep(1)
    ingresovalido = False
    while(ingresovalido==False):
        print "Porfavor seleccione su tipo de membresia: \n1. Gold\n2. Silver\n3. Ninguno\n"
        tipo = raw_input("Escoja su membresia (1-3): ")
        if compnum(tipo)!="Invalido":
            
            if tipo =="1":
                descuento = .05
                while (fincompra == False):
                    productocompra = raw_input("Ingrese producto a comprar: ")
                    productocompra = productocompra.lower()
                    if productocompra in inventario:
                        factura.append(productocompra)
                        #factura[productocompra]=inventario[productocompra]
                        for x,y in inventario[productocompra].items():
                            total = total+((x+y)*(1-descuento))
                        #print total
                        otracompra = False
                        while (otracompra == False):
                            respuesta = raw_input("Otra compra? Si/no ")
                            otracompra = compresp(respuesta)
                            if otracompra == False:
                                print "Ingreso incorrecto. Solo se admite si/no"
                        if respuesta == "si":
                            fincompra = False
                        elif respuesta == "no":
                            fincompra = True
                        else:
                            print "Respuesta incorrecta. Solo se admite si/no"
                    else:
                        print "Ese producto no existe"

                print "Facturando su compra, porfavor espere..."
                time.sleep(2)
                print "\nFavor de cancelar Q"+ str(total)+" por el consumo de:"
                for x in factura:
                    for y,z in inventario[x].items():
                            descontado = (z+y)*descuento
                            print "\n-Producto: ", x, "."
                            print "Valor sin iva: ", y, ". Iva: ", z, ". Descuento: ", descontado, ". Total: ", (z+y)*(1-descuento)
                print "\nTotal compra: ", total
                nuevafactura()
                ingresovalido = True
                time.sleep(3)

            elif tipo =="2":
                descuento = .03
                while (fincompra == False):
                    productocompra = raw_input("Ingrese producto a comprar: ")
                    productocompra = productocompra.lower()
                    if productocompra in inventario:
                        factura.append(productocompra)
                        #factura[productocompra]=inventario[productocompra]
                        for x,y in inventario[productocompra].items():
                            total = total+((x+y)*(1-descuento))
                        #print total
                        otracompra = False
                        while (otracompra == False):
                            respuesta = raw_input("Otra compra? Si/no ")
                            otracompra = compresp(respuesta)
                            if otracompra == False:
                                print "Ingreso incorrecto. Solo se admite si/no"
                        if respuesta == "si":
                            fincompra = False
                        elif respuesta == "no":
                            fincompra = True
                        else:
                            print "Respuesta incorrecta. Solo se admite si/no"
                    else:
                        print "Ese producto no existe"

                print "Facturando su compra, porfavor espere..."
                time.sleep(2)
                print "\nFavor de cancelar Q"+ str(total)+" por el consumo de:"
                for x in factura:
                    for y,z in inventario[x].items():
                            descontado = (z+y)*descuento
                            print "\n-Producto: ", x, "."
                            print "Valor sin iva: ", y, ". Iva: ", z, ". Descuento: ", descontado, ". Total: ", (z+y)*(1-descuento)
                print "\nTotal compra: ", total
                nuevafactura()
                ingresovalido = True
                time.sleep(3)
            elif tipo == "3":
                descuento = 1
                while (fincompra == False):
                    productocompra = raw_input("Ingrese producto a comprar: ")
                    productocompra = productocompra.lower()
                    if productocompra in inventario:
                        factura.append(productocompra)
                        #factura[productocompra]=inventario[productocompra]
                        for x,y in inventario[productocompra].items():
                            total = total+((x+y)*(1-descuento))
                        #print total
                        otracompra = False
                        while (otracompra == False):
                            respuesta = raw_input("Otra compra? Si/no ")
                            otracompra = compresp(respuesta)
                            if otracompra == False:
                                print "Ingreso incorrecto. Solo se admite si/no"
                        if respuesta == "si":
                            fincompra = False
                        elif respuesta == "no":
                            fincompra = True
                        else:
                            print "Respuesta incorrecta. Solo se admite si/no"
                    else:
                        print "Ese producto no existe"

                print "Facturando su compra, porfavor espere..."
                time.sleep(2)
                print "\nFavor de cancelar Q"+ str(total)+" por el consumo de:"
                for x in factura:
                    for y,z in inventario[x].items():
                            descontado = (z+y)*descuento
                            print "\n-Producto: ", x, "."
                            descontado = "\"No eres miembro. UNETE YA AL +502 QUIERODESCUENTOS\""
                            print "\n-Producto: ", x, "."
                            print "Valor sin iva: ", y, ". Iva: ", z, ". Descuento: ", descontado, ". Total: "
                nuevafactura()
                time.sleep(3)
                ingresovalido = True
            else:
                print "Ingreso incorrecto, seleccione 1 a 3"
        else:
            print "Ingreso incorrecto. Solo se permiten numeros."

    
#*****************************Diccionarios*************************
inventario = {} #diccionario de articulos y precios
factura=[] #listado de articulos a comprar

#************************Programa principal(Main)******************


opcion = menu()
while opcion!="0":
    if opcion == "1":
    #Ingreso
        ingresarmas = False
        finingreso = False
        ingresocorrecto = "Invalido"
        while(finingreso==False):
            while (ingresocorrecto!="Int"):
                cantidadingreso = raw_input("Ingrese cantidad de productos a ingresar: ")
                ingresocorrecto=compnum(cantidadingreso)
                if (ingresocorrecto=="Int"):
                    cantidadingreso = int(cantidadingreso)
                else:
                    print "Ingreso invalido. Vuelva a intentarlo"
                    ingrescorrecto = "Invalido"
            while (cantidadingreso>0):
                producto = raw_input("Ingrese producto: ")
                producto = producto.lower()
                preciovalido="Invalido"
                while (preciovalido=="Invalido"):
                    precio = raw_input("Ingrese precio: ")
                    preciovalido = compnum(precio)
                    if preciovalido == "Invalido":
                        print "Solo se permiten numeros reales. Vuelva a ingresar precio"
                    elif preciovalido == "Float" or preciovalido == "Int":
                        precio = float(precio)
                #Guardando iva y precio por separado
                iva = precio*.12
                #precio = precio + iva
                inventario[producto] = {precio:iva}
                print producto, "ingresado, su precio es de Q"+ str(precio), iva
                cantidadingreso-=1
        
            while(ingresarmas==False):
                respuesta = raw_input("Desea ingresar mas productos y precios? Si/no ")
                ingresarmas = compresp(respuesta)
                if ingresarmas == False:
                    print "Ingrese solo si o no. Vuelve a intentarlo."
                elif ingresarmas == True:   
                    ingresarmas = True
            if respuesta== "si" :
				finingreso = False
				ingresocorrecto = "Invalido"
            elif respuesta == "no":
                finingreso = True

            

    elif opcion == "2":
        compra()
    elif opcion == "3":
        mostrarinventario()
    elif opcion=="4":
        print "Saliendo"
        break
    
    
    opcion = menu()
