from os import system, name 
from time import sleep 

n = 1 #numero de pizzas
total = 0 #total a pagar
tamano = {'grande':580,'mediana':430,'personal':280}                   #diccionario de tamanos, con el nombre como clave y el precio como valor
toppings = {'jamon':40,'champinon':35,'pimenton':30,'extraqueso':40,   #diccionario de toppings, con el nombre como clave y el precio como valor
            'aceitunas':58,'pepperoni':38.5,'salchichon':62.5}
bebidas = {'refresco':100,'limonada':45,'vino':185,'nestea':80,'frappe':50,'cafe':25}
resumen_ingredientes = []
resumen_tamanos = []
resumen_subtotal = []

def clear():                    #funcion para limpiar pantalla
    if name == 'nt': 
        _ = system('cls')   #para windows
    else: 
        _ = system('clear')     #para linux

def logo():
    print(' \t\t ------------------------------------------')
    print('\t\t|  * *                                * *  |')
    print('\t\t|  *   *          PIZZERIA          *   *  |')
    print('\t\t|  *     *          UCAB          *     *  |')
    print('\t\t|  * *  *  *                    *  *  * *  |')
    print(' \t\t ------------------------------------------')

def menu_inicio():
     
     clear()
     logo()
     print("\tPizza numero:",n)              #toma el valor de la variable global n para contabilizar el numero total de pizzas
     print('\tOpciones de TAMAÑO:')
     print('\t\t( 1 )Grande\t( 2 )Mediana\t( 3 )Personal')
     opcion = input('\tIndique una opcion(1/2/3): ')   #permite al usuario escoger una opcion entre los 3 tipos de tamanos disponibles
 
     if opcion == "1":
         subtotal = tamano.get('grande')       #se le suma al subtotal el precio establecido para cada tipo de tamano cuyo valor esta almacenado 
         menu_toppings('grande',subtotal)      #en el diccionario tamano
     elif opcion == "2":
        subtotal = tamano.get('mediana')
        menu_toppings('mediana',subtotal)
     elif opcion == "3":
        subtotal = tamano.get('personal')
        menu_toppings('personal',subtotal)
     else:
        print('OPCION INVALIDA. Intente nuevamente')    #en caso de obtener un valor incorrecto se llama recursivamente a la funcion que contiene el menu inicial 
        sleep(1)
        menu_inicio()

def menu_toppings(tamano_p,subtotal):
    clear()
    logo()
    lista_ingredientes = []      #se crea una lista que guarde los ingredientes escogidos para cada pizza para mostrarlos todos al final de cada orden
    opcion = None
    print("\tPizza numero:",n)
    print("\tTamaño: ", tamano_p.upper())
    print("\n\tMenu de Toppings:")
    print("\t\tJamon\t\t( 1 )")
    print("\t\tPimenton\t( 2 )")
    print("\t\tDoble queso\t( 3 )")
    print("\t\tAceitunas\t( 4 )")
    print("\t\tPepperoni\t( 5 )")
    print("\t\tSalchichon\t( 6 )")
    print("\t\tChampinones\t( 7 )\n")
    
    #mediante un ciclo while el usuario podra escoger tantos ingredientes como quiera hasta que el ciclo se acabe
    #  cuando el usuario ingrese la tecla ENTER 
    while opcion != "":
        opcion = input('\tIndique ingredientes (enter para continuar): ') 
        if opcion == "1":                                                 
            subtotal = subtotal + toppings.get("jamon")   #por cada opcion de topping disponible, se sumara al subtotal el precio del cada uno
            lista_ingredientes.append("jamon")            #este precio se encuentra como valor en el diccionario global llamado toppings
        elif opcion =="2":                                #por lo que obtenemos el valor del precio al indicar la clave mediante la funcion get() de los diccionarios
            subtotal = subtotal + toppings.get("pimenton")
            lista_ingredientes.append("pimenton")
        elif opcion =="3":
            subtotal = subtotal + toppings.get("extraqueso")
            lista_ingredientes.append("doble queso")
        elif opcion =="4":
            subtotal = subtotal + toppings.get("aceitunas")
            lista_ingredientes.append("aceitunas")
        elif opcion == "5":
            subtotal = subtotal + toppings.get("pepperoni")
            lista_ingredientes.append("pepperoni")
        elif opcion == "6":
            subtotal = subtotal + toppings.get("salchichon")
            lista_ingredientes.append("salchichon")
        elif opcion == "7":
            subtotal = subtotal + toppings.get("champinon")
            lista_ingredientes.append("champinones")
        elif opcion == "":
            orden(tamano_p,lista_ingredientes,subtotal) 
        else:
             print("\t\tOPCION INVALIDA. Intente nuevamente") #en caso de que se ingrese un caracter erroneo, se le notificara al usuario 

def menu_bebida():
    clear()
    logo()
    global total
    lista_bebidas = []
    subtotal = 0
    opcion = " "
    print("\tOpciones de bebida:")
    print("\t\tRefresco:\t( 1 )")
    print("\t\tLimonada:\t( 2 )")
    print("\t\tVino:\t\t( 3 )")
    print("\t\tNestea:\t\t( 4 )")
    print("\t\tFrappe:\t\t( 5 )")
    print("\t\tCafe:\t\t( 6 )")
    while opcion != "":
        opcion = input('\tIndique bebidas (enter para continuar): ') 
        if opcion == "1":                                                 
            subtotal = subtotal + bebidas.get("refresco")   #por cada opcion de topping disponible, se sumara al subtotal el precio del cada uno
            lista_bebidas.append("refresco")            #este precio se encuentra como valor en el diccionario global llamado bebidas
        elif opcion =="2":                                #por lo que obtenemos el valor del precio al indicar la clave mediante la funcion get() de los diccionarios
            subtotal = subtotal + bebidas.get("limonada")
            lista_bebidas.append("limonada")
        elif opcion =="3":
            subtotal = subtotal + bebidas.get("vino")
            lista_bebidas.append("vino")
        elif opcion =="4":
            subtotal = subtotal + bebidas.get("nestea")
            lista_bebidas.append("nestea")
        elif opcion == "5":
            subtotal = subtotal + bebidas.get("frappe")
            lista_bebidas.append("frappe")
        elif opcion == "6":
            subtotal = subtotal + bebidas.get("cafe")
            lista_bebidas.append("cafe")
        elif opcion == "":
            total = total + subtotal
            return lista_bebidas
        else:
             print("\t\tOPCION INVALIDA. Intente nuevamente") #en caso de que se ingrese un caracter erroneo, se le notificara al usuario 

def resumen():
    cont=0
    while cont < len(resumen_tamanos):
        print("\n\t\tPizza #",cont+1)
        print("\t\tTamano: ",*resumen_tamanos[cont].upper())
        if resumen_ingredientes[cont] == "Margarita":
            print("\t\tTipo: MARGARITA")
        else:
            print("\t\tToppings: ", end="")
            print(*resumen_ingredientes[cont], sep = ", ")
        print("\t\tSubtotal: ",resumen_subtotal[cont], "Bs")
        cont=cont+1
    print("\n")



def orden(tamano_p,toppings_p,subtotal_p): #esta funcion muestra un resumen de la pizza que se esta pidiendo actualmente, indicando subtotal y toppings agregados
    clear()
    logo()
    nueva = ""
    global n        #ya que estamos modificando una variable global, es necesario anadir la constante "global" seguido del nombre de la variable dentro de la funcion
    global total
    global resumen_ingredientes
    global resumen_tamanos
    global resumen_subtotal
    resumen_tamanos.append(tamano_p)
    listaux2 = ""
    iva = lambda x: x*1.16   # esta funcion lambda permitira calcular el iva del valor que le pasemos como parametro 
    bebida_op = ""
    print("\tPizza numero:",n)
    print("\tTamano: ",tamano_p.upper()) #para mostrar el tamano en mayusculas
    total = total + subtotal_p  #en esta linea se suma el subtotal de la orden especifica al total a pagar por todas las pizzas ordenadas, en caso de ser varias
    if not toppings_p:              #este condicional if nos permite saber si la pizza posee toppings o no, mediante la lista de toppings de la funcion anterior
        print("\tTipo: MARGARITA")       #pasada como parametro
        resumen_ingredientes.append("Margarita")
    else:                                          #en caso de que SI hallan toppings, se mostraran 
        listaux = [x.upper() for x in toppings_p]  #mediante comprehension lists se crea una lista que muestre los toppings anadidos, pero en mayuscula 
        print("\tToppings: ", end="")
        print(*listaux, sep = ", ")
        resumen_ingredientes.append(listaux)
     
    print("\tSubtotal: ",subtotal_p,"Bs")
    resumen_subtotal.append(subtotal_p)   
        
    while nueva != "s" or nueva != "n":
        nueva = input("\t\tDesea ordenar otra pizza?[s/n]")
        if nueva == "s":
            n=n+1               #en caso de que se deseen ordenar mas pizzas, se llama a la funcion del menu de inicio y se incrementa la variable global n,
            menu_inicio()       #que representa el numero de pizzas ordenadas
        elif nueva == "n":
            while bebida_op != "s" or bebida_op != "n":
                bebida_op = input("\t\tDesea ordenar bebidas?[s/n]")
                if bebida_op == "s":
                    bebidas = menu_bebida()
                    listaux2 = [x.upper() for x in bebidas]  #mediante comprehension lists se crea una lista que muestre las bebidas escogidas en mayuscula 
                    break
                elif bebida_op == "n":
                    break
                else: 
                    print("\t\tOPCION INVALIDA. Intente nuevamente")
            clear()
            logo()
            print("\t\tCantidad de pizzas: ",n) #en caso contrario, si no se desean ordenar mas pizzas, se mostrara la cantidad total de pizzas
            resumen()
            if listaux2 != None:
                print("\t\tBebidas: ", end="")
                print(*listaux2, sep = ", ")
            else:
                break
            print("\n\t\tTotal:",total,"Bs") #y el monto total a cancelar, obtenido como resultado de sumar los subtotales de cada orden
            print("\t\tTotal a pagar(+IVA):",format(iva(total),"0.2f"),"Bs")
            print("\t\tGracias por su compra, regrese pronto")
            close = " "
            while close!="s" or close != "n":
                close = input("\n\t\t¿Desea cerrar la tienda?[s/n]: ")
                if close == "s":
                    exit()
                elif close == "n":
                    n=1
                    total=0
                    resumen_ingredientes = []
                    resumen_tamanos = []
                    resumen_subtotal = []
                    menu_inicio()
                else:
                    print("\t\tOPCION INVALIDA. Intente nuevamente")

            exit()
        else:
            print("\t\tOPCION INVALIDA. Intente nuevamente")
         
     
menu_inicio() #inicio del programa al llamar a la funcion del menu inicial, si no se llamara la funcion, el programa nunca empezaria