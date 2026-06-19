peliculas=[
    {"titulo": "Inception", "director": "Christopher Nolan",
     "genero": "Ciencia Ficcion", "anio": 2010, "rate": 8.9 },
    {"titulo": "Jurassic Park", "director": "Steven Spilberg",
     "genero": "Ciencia Ficcion", "anio": 1993 , "rate": 9.6},
    {"titulo": "Se7en", "director": "David Fincher",
     "genero": "Thiller", "anio": 1997 , "rate": 9.3},
]
def quitarPeli():
    titulo=input("ingrese el titulo de la pelicula a eliminar")
    for peli in peliculas:
        if peli["titulo"].lower()==titulo.lower():
            peliculas.remove(peli)
            print("pelicula eliminada")
            break
    else:
        print("pelicula no encontrada")

def mostrarPeliculas():
    for peli in peliculas:
        print(f"{peli['titulo']} - {peli['director']} - {peli['genero']} - {peli['año']} - {peli['rate']}")

def mostrarTitulos():
    for peli in peliculas:
        print(peli["titulo"])
    
def mostrarños():
    aos = []
    for peli in peliculas:
        aos.append(peli["año"])
    aos.sort()
    for años in aos:
        print(años)

def mostrarMejorCalificada():
    mejor_peli = max(peliculas, key=lambda x: x["rate"])
    print(f"La pelicula mejor calificada es: {mejor_peli['titulo']} con una calificacion de {mejor_peli['rate']}")

def ingresarPelicula():
    titulo=input("ingrese el titulo de la pelicula")
    if len(titulo)<3:
        print("el titulo debe tener mas de 2 caracteres")
        return
    director=input("ingrese el director de la pelicula")
    if len(director.split())<2:
        print("el director debe tener nombre y apellido")
        return
    genero=input("ingrese el genero de la pelicula")
    anio=int(input("ingrese el año de la pelicula"))
    if anio<1960 or anio>2024:
        print("el año debe ser mayor a 1960 y menor al año actual")
        return
    rate=float(input("ingrese la calificacion de la pelicula"))
    peliculas.append({"titulo": titulo, "director": director, "genero": genero, "anio": anio, "rate": rate})
    print("pelicula ingresada correctamente")

def actualizarPelicula():
    titulo=input("ingrese el titulo de la pelicula a actualizar")
    for peli in peliculas:
        if peli["titulo"].lower()==titulo.lower():
            nuevo_titulo=input("ingrese el nuevo titulo de la pelicula")
            if len(nuevo_titulo)<3:
                print("el titulo debe tener mas de 2 caracteres")
                return
            nuevo_director=input("ingrese el nuevo director de la pelicula")
            if len(nuevo_director.split())<2:
                print("el director debe tener nombre y apellido")
                return
            nuevo_genero=input("ingrese el nuevo genero de la pelicula")
            nuevo_anio=int(input("ingrese el nuevo año de la pelicula"))
            if nuevo_anio<1960 or nuevo_anio>2024:
                print("el año debe ser mayor a 1960 y menor al año actual")
                return
            nuevo_rate=float(input("ingrese la nueva calificacion de la pelicula"))
            peli["titulo"]=nuevo_titulo
            peli["director"]=nuevo_director
            peli["genero"]=nuevo_genero
            peli["anio"]=nuevo_anio
            peli["rate"]=nuevo_rate
            print("pelicula actualizada correctamente")
            break


    else:
        print("pelicula no encontrada")

def menu():
    while True:
        try:
            print("PELICULAS")
            print('''1.- ingresar Pelicula
    2.- quitar Pelicula
    3.- Actualizar Pelicula
    4.- Mostrar Peliculas
    5.- Mostrar solo los titulos
    6.- Mostrar los aos de las peliculas ordenados
    7.- Mostrar meplicula mejor calificada
    8.- Salir
    ''')
            op=int(input("seleccione una opcion: "))
            match op:
                case 1:
                    ingresarPelicula()
                case 2:
                    quitarPeli()
                case 3:
                    actualizarPelicula()
                case 4:
                    mostrarPeliculas()
                case 5:
                    mostrarTitulos()
                case 6:
                    mostrarños()
                case 7:
                    mostrarMejorCalificada()
                case 8:
                    print("saliendo...")
                    break
        except ValueError as e:
            print("error, ", e)


menu()
