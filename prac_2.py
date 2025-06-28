# exp 1: Se inicia un programa python creando una lista que contiene dentro, diccionarios.
# exp 2: Se puede entender como una lista normal, pero que en cada posicion podemos acceder a un dicciario de una pelicula diferente

#En resumen se crea una lista la cual por dentro contiene diccionarios.

# Ejemplo:
# listaRandom = [1, 2 ,3 ,4 ,5] --> Para ejemplificar hicimos eso pero con {}, osea diccionarios.

peliculas = [{
    "nombre": "Rapidos y furiosos",
    "genero": "accion",
    "estreno": 2003,
    "puntuacion": 10
},
{
    "nombre": "Minecraft: The movie",
    "genero": "fantasia",
    "estreno": 2025,
    "puntuacion": 9.5
},
{
    "nombre": "Donde estan las rubias",
    "genero": "comedia",
    "estreno": 2007,
    "puntuacion": 10
},]


# Se crea una funcion la cual se va utilizar para agregar una nueva pelicula a la lista de diccionarios de peliculas
# --> Se indica que el parametro que va recibir nuestra funcion va ser una lista de peliculas, del tipo (list)
def agregarPelicula(listaPeliculas: list): 
    cantAgregar = int(input("Cuantas peliculas desea agregar: "))
    for i in range(cantAgregar):
        nombre = input("Ingrese el nombre de la pelicula a agregar: ")
        genero = input("Ingrese el genero de la pelicula a agregar: ")
        estreno = int(input("Ingrese fecha de estreno de la pelicula: "))
        puntuacion = float(input("Ingrese puntuacion de la pelicula: "))

        # Aqui se crea un diccionario, el cual representar nuestra nueva pelicula a agregar a nuestra lista de diccionarios
        # Donde mantenemos nuestra plantillas de llaves, pero se le pasa como valor las variables que anteriormente creamos con sus input
        nuevaPelicula = {
            "nombre": nombre,
            "genero": genero,
            "estreno": estreno,
            "puntuacion": puntuacion
        }

        # Al parametro que pedimos en nuestra funcion le invocamos el metodo append, para agregar la nueva pelicula que el usuario desee ingresar
        listaPeliculas.append(nuevaPelicula)
        print("La pelicula ha sido agregada correctamente!")
    return listaPeliculas

def mostrarPeliculas(lista): 
    for p in lista:
        print(f"{p}") 

# Se indica que ahora la lista peliculas sera igual al valor que retorna nuestra funcion
# Es decir lo que se hace es autoinvocar la funcion pero tambien asignar el valor que nos devuelva esa funcion, es decir, lo que antes hicimos con el return
peliculas = agregarPelicula(peliculas)

print("LISTA POR DEFECTO SIN ORDENAR")
mostrarPeliculas(peliculas)

listaOrdenadaAbcdario = sorted(peliculas, key=lambda nombre : nombre["nombre"])
listaOrdenadaGenero = sorted(peliculas, key=lambda gen : gen["genero"])
listaOrdenadaEstreno = sorted(peliculas, key=lambda est : est["estreno"])
listaOrdenadaPuntuacion = sorted(peliculas, key=lambda pun : pun["puntuacion"])

print("LISTA ORDENADA POR ABECEDARIO\n", listaOrdenadaAbcdario, "\n")
print("LISTA ORDENADA POR GENERO\n", listaOrdenadaGenero, "\n")
print("LISTA ORDENADA POR FECHA ESTRENO\n", listaOrdenadaEstreno, "\n")
print("LISTA ORDENADA POR PUNTUACION\n", listaOrdenadaPuntuacion)

