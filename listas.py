# listas=[2 ,7 ,9 , 2, 3.8]
# print(listas)
# print(listas[4])

# name="cristian"
# for i in listas:
#     print(i)

#cree un alista de cuatro futras y muestrelas en pantalla
# lista=["Uva", "pera", "naranja", "kiwi"]
# ccv=0
# for i in lista:

#     if i[0].lower() in ("aeiou"):
#         print(f"esta es la fruta {i} comienza con una vocal")
#         ccv+=1
#     else:
#         print(f"esta fruta es {i} ")
# print("esta es la cantidad de furtas que comienzan con vocales, ", ccv )

# nombres=["cris", "dante", "paz"]
# apellidos=["acuña", "rojas", "carejos"]

  

# print("==estos son los nombres== ")
# for i in nombres:
#     print(i)
# print("==estos son los apellidos==  ")

# for i in apellidos:
#     print(i)    

# nombres=["cristian", "dante", "maria paz"]
# apellidos=["acuña", "rojas", "carrejos"]

  

# print("==estos son los nombres y apellidos== ")
# for i in range(len (apellidos)):
#     print(nombres[i], apellidos[i])

# nombres.append("gonzalo")
# apellidos.append("milan")



# print("==estos son los nombres y apellidos== ")
# for i in range(len (apellidos)):
#     print(nombres[i], apellidos[i])



#crea un alista de animales con 3 elementos 
#agrege dos elementos
#y mustre el resultado de la misma 

# con=0

# animales=["gato", "perro", "gaviota"]

# print("===lista de animales=== ")
# for i in animales:
#     con+=1
#     print(con, i)



# animales.insert(0,"cancho")
# animales.insert(2,"jabali")
# print("===esta es la nueva lista de animales ===")
# con=0


# for i in animales:
#     con+=1
#     print(con, i)
    


# alumno={
#     "nombre:": "masca pitos ",
#     "carrera:": "informaica",
#     "edad:": 18
# }
# print(alumno)
# for key, value in alumno.items():
#     print(key, value)
op=0

vegetales={
    1:"maracuya",
    2:"pera",
    3:"cebolla",
}

def agregarVegetal():
    nombrev=input("ingrese el nombre de la vegetal: ")
    vegetales[list(vegetales.items())[-1][0]+1]=(nombrev)
    

def mostrarVegetal():
    for key, value in vegetales.items():
        print(key,".-",value )
    print("-"*30)

 
def eliminarVegetal():
    bolal=int(input("ingrese el numero el que quiera eliminiar: "))
    del vegetales[bolal]
    

def actualizarVegeteal():
    print("")


def vegetalesMenu():
    while True:
        try:
            print("====FERIA====")
            print("1. agregar vegetal ")
            print("2. eliminar vegetal ")
            print("3. acualizar vegetal ")
            print("4. mostrar vegetal ")
            print("5. --salir--")
            op=int(input("seleccione una opcion "))
            match op:
                case 1:
                    agregarVegetal()
                case 2:
                    eliminarVegetal()
                case 3:
                    actualizarVegeteal()
                case 4:
                    mostrarVegetal()
                case 5:
                    print("saliendo")
                    break
        except:
            print("error intente denuevo ")



vegetalesMenu()