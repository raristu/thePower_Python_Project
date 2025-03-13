''' PROYECTO LÓGICA: Katas de Python '''
# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. 
# Los espacios no deben ser considerados.

texto = "raul aristu"

def frecuencias(texto):
    diccionario = {}
    for letra in texto:
        if letra != " ": # Si la letra no es un espacio
            if letra in diccionario:
                diccionario[letra] += 1
            else:
                diccionario[letra] = 1
    return diccionario

print(frecuencias(texto))


# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

numeros = [1, 2, 3, 4, 5]

def doble(numeros):
    return list(map(lambda x: x * 2, numeros)) # Multiplica cada número por 2

print(doble(numeros))

# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. 
# La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

palabras = ["hola", "adios", "alto", "bajo", "hola", "arbol", "planta"]
objetivo = "hola"

def contiene(palabras, objetivo): 
    return list(filter(lambda x: objetivo in x, palabras)) # Devuelve las palabras que contienen el objetivo

print(contiene(palabras, objetivo))

#4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

lista1 = [1, 2, 3, 4, 5]
lista2 = [5, 4, 3, 2, 1]

def diferencia(lista1, lista2):
    return list(map(lambda x, y: x - y, lista1, lista2)) # Resta los valores de las dos listas

print(diferencia(lista1, lista2))

#5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
# defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
# que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
# una tupla que contenga la media y el estado.

lista_numeros = [5, 6, 7, 8, 9, 10]
nota_aprobado = 5

def estado(lista_numeros, nota_aprobado = 5):
    media = sum(lista_numeros) / len(lista_numeros)
    if media >= nota_aprobado: # Si la media es mayor o igual que la nota de aprobado
        return (media, "aprobado")
    else:
        return (media, "suspenso")

print(estado(lista_numeros, nota_aprobado))

#6. Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1) # Llamada recursiva

print(factorial(4))

# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

lista_tuplas = [(1, 2), (3, 4), (5, 6)]

def convertir(lista_tuplas):
    return list(map(lambda x: str(x[0]) + str(x[1]), lista_tuplas)) # Convierte las tuplas a strings

print(convertir(lista_tuplas))

# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
# o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
# indicando si la división fue exitosa o no.

def division():
    try:
        num1 = int(input("Introduce un número: "))
        num2 = int(input("Introduce otro número: "))
        resultado = num1 / num2
        print(f"La división fue exitosa y el resultado es: {resultado}")
    except ValueError: # Si el usuario introduce un valor no numérico
        print("Debes introducir un número")
    except ZeroDivisionError:   # Si el usuario intenta dividir por cero
        print("No puedes dividir por cero")

division()

# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
# excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
# "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

mascotas = ["Perro", "Gato", "Mapache", "Loro", "Serpiente Pitón", "Canario", "Tortuga", "Cocodrilo", "Oso"]
prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

def mascotas_prohibidas(mascotas):    
    return list(filter(lambda x: x not in prohibidas, mascotas))    # Devuelve las mascotas que no están prohibidas

print(mascotas_prohibidas(mascotas))

# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
# excepción personalizada y maneja el error adecuadamente.

lista_numeros1 = [1, 2, 3, 4, 5]
lista_vacia = []

def promedio(lista):
    try:    # Intenta calcular el promedio
        return sum(lista)/len(lista) # Suma los números y divide por la cantidad de números
    except ZeroDivisionError:  # Si la lista está vacía
        raise Exception("La lista está vacía")

print(promedio(lista_numeros1))
print(promedio(lista_vacia))  

# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
# valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones
# adecuadamente.

def edad():
    try:
        edad = int(input("Introduce tu edad: "))
        if edad < 0 or edad > 120: # Si la edad es menor que 0 o mayor que 120
            raise ValueError # Lanza una excepción
        else:
            print(f"Tu edad es: {edad}")
    except ValueError:  # Si el usuario introduce un valor no numérico o fuera del rango
        print("Debes introducir un número válido entre 0 y 120")

edad()

# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def longitud(frase):
    return list(map(lambda x: len(x), frase.split())) # Devuelve la longitud de cada palabra

print(longitud("Hola mundo me llamo Raul"))

# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
# mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map()

def mayusculas_minusculas(texto):
    return list(map(lambda x: (x.upper(), x.lower()), set(texto))) # Devuelve las letras en mayúsculas y minúsculas

print(mayusculas_minusculas("raul"))

# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la
# función filter()

lista_palabras = ["hola", "adios", "alto", "bajo", "hola", "arbol", "planta"]
letra = "a"

def comienza_con(lista_palabras, letra):
    return list(filter(lambda x: x[0] == letra, lista_palabras))    # Devuelve las palabras que comienzan con la letra indicada

print(comienza_con(lista_palabras, letra))

# 15. Crea una función lambda que sume 3 a cada número de una lista dada.

lista_dada = [10, 20, 30, 40, 50]

def suma_tres(lista):
    return list(map(lambda x: x + 3, lista))    # Suma 3 a cada número

print(suma_tres(lista_dada))

# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
# todas las palabras que sean más largas que n. Usa la función filter()

texto = "Hola mundo me llamo Raul"
n = 4

def palabras_mas_largas(texto, n):
    return list(filter(lambda x: len(x) > n, texto.split()))    # Devuelve las palabras más largas que n

print(palabras_mas_largas(texto, n))

# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]
# corresponde al número quinientos setenta y dos (572). Usa la función reduce()

from functools import reduce    # Importa la función reduce de la librería functools

lista_digitos = [5, 7, 2]

def numero_correspondiente(lista):
    return reduce(lambda x, y: x * 10 + y, lista)   # Devuelve el número correspondiente

print(numero_correspondiente(lista_digitos))

# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
# (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a
# 90. Usa la función filter()

def calificacion_estudiantes(estudiantes):
    return list(filter(lambda x: x["calificacion"] >= 90, estudiantes))     # Devuelve los estudiantes con calificación mayor o igual a 90

print(calificacion_estudiantes([{"nombre": "Raul", "edad": 25, "calificacion": 100},
                                {"nombre": "Javier", "edad": 23, "calificacion": 80},
                                {"nombre": "María", "edad": 30, "calificacion": 95}]))

# 19. Crea una función lambda que filtre los números impares de una lista dada.

lista_impares = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def impares(lista):
    return list(filter(lambda x: x % 2 != 0, lista))    # Devuelve los números impares

print(impares(lista_impares))

# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función
# filter()

lista_elementos = [1, "hola", 2, "adios", 3, "alto", 4, "bajo", 5, "hola", 6, "arbol", 7, "planta"]

def solo_int(lista):
    return list(filter(lambda x: type(x) == int, lista))    # Devuelve los valores enteros

print(solo_int(lista_elementos))

# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda

numero = 3

def cubo(numero):
    return (lambda x: x ** 3)(numero)   # Calcula el cubo del número

print(cubo(numero))

# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .

lista_numerica = [1, 2, 3, 4, 5]

def producto_total(lista):
    return reduce(lambda x, y: x * y, lista)    # Devuelve el producto total de los valores de la lista

print(producto_total(lista_numerica))

# 23. Concatena una lista de palabras.Usa la función reduce() .

lista_palabras = ["Hola", "mundo", "me", "llamo", "Raul"]

def concatenar(lista):
    return reduce(lambda x, y: x + " " + y, lista)  # Concatena las palabras

print(concatenar(lista_palabras))

# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .

lista_valores = [1, 2, 3, 4, 5]

def diferencia_total(lista):
    return reduce(lambda x, y: x - y, lista)    # Calcula la diferencia total

print(diferencia_total(lista_valores))

# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

cadena_texto = "Hola mundo"

def contar_caracteres(cadena):
    return len(cadena)  # Devuelve el número de caracteres

print(contar_caracteres(cadena_texto))

# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.

numero1 = 10
numero2 = 3 

def resto(numero1, numero2):
    return (lambda x, y: x % y)(numero1, numero2)   # Calcula el resto de la división

print(resto(numero1, numero2))

# 27. Crea una función que calcule el promedio de una lista de números.

lista_numeros2 = [1, 2, 3, 4, 5]

def promedio(lista):
    return sum(lista) / len(lista)  # Calcula el promedio

print(promedio(lista_numeros2)) 

# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

lista_dada = [5, 2, 3, 4, 5, 6, 2, 8, 9, 1]

def duplicado(lista):
    return next((x for x in lista if lista.count(x) > 1), None)     # Devuelve el primer elemento duplicado

print(duplicado(lista_dada))

# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
# carácter '#', excepto los últimos cuatro.

def enmascarar(variable):
    cadena = str(variable)
    if len(cadena) <= 4:    
        return cadena       # Si la cadena tiene 4 caracteres o menos, no se enmascara
    else:
        return "#" * (len(cadena) - 4) + cadena[-4:]    # Enmascara todos los caracteres excepto los últimos cuatro

print(enmascarar(1234567890123456))
print(enmascarar("Hola me llamo Raul"))
print(enmascarar(1234))

# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
# pero en diferente orden.

palabra1 = "sal"
palabra2 = "las"

def anagramas(palabra1, palabra2):
    return sorted(palabra1) == sorted(palabra2)     # Devuelve si las palabras son anagramas

print(anagramas(palabra1, palabra2))

# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
# esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
# lanza una excepción.

def buscar_nombre():
    try:    # Intenta buscar el nombre
        lista_nombres = input("Introduce una lista de nombres separados por comas: ").split(",")    # Introduce los nombres separados por comas
        nombre = input("Introduce un nombre a buscar: ")    # Introduce el nombre a buscar
        if nombre in lista_nombres:     
            print("El nombre fue encontrado")   # Si el nombre está en la lista, se imprime un mensaje
        else:
            raise Exception("El nombre no fue encontrado")  # Si el nombre no está en la lista, se lanza una excepción
    except Exception as e:  
        print(e)    # Muestra el mensaje de la excepción
    
buscar_nombre()

# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
# devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
# no trabaja aquí.

nombre_completo = 'Raul Aristu'
empleados = [
            ('Pepe Martínez', 'Abogado'),
            ('Raul Aristu', 'Analista de Datos'),
            ('Javier López', 'Ingeniero')]

def buscar_puesto(nombre_completo, empleados):  # Busca el nombre completo en la lista de empleados
    for empleado in empleados:
        if nombre_completo in empleado:
            return empleado[1]  # Devuelve el puesto del empleado, si está en la lista
    return "La persona no trabaja aquí"     # Si la persona no está en la lista, devuelve un mensaje

print(buscar_puesto(nombre_completo, empleados))

# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

lista1 = [1, 2, 3, 4, 5]
lista2 = [5, 4, 3, 2, 1]

sumar_listas = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))   # Suma los elementos correspondientes de las dos listas

print(sumar_listas(lista1, lista2))

# 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
# crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
# manipular la estructura del árbol.
# Código a seguir:
# 1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
# 2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
# 3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
# 4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
# 5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
# 6. Implementar el método # info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las # mismas.
# Caso de uso:
# 1. Crear un árbol.
# 2. Hacer crecer el tronco del árbol una unidad.
# 3. Añadir una nueva rama al árbol.
# 4. Hacer crecer todas las ramas del árbol una unidad.
# 5. Añadir dos nuevas ramas al árbol.
# 6. Retirar la rama situada en la posición 2.
# 7. Obtener información sobre el árbol.

class Arbol:    # Define la clase Arbol
    def __init__(self):     # Inicializa el árbol
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):    # Aumenta la longitud del tronco en una unidad 
        self.tronco += 1

    def nueva_rama(self):   # Añade una nueva rama de longitud 1 a la lista de ramas
        self.ramas.append(1)

    def crecer_ramas(self):     # Aumenta en una unidad la longitud de todas las ramas existentes
        self.ramas = [x + 1 for x in self.ramas]

    def quitar_rama(self, posicion):    # Elimina una rama en una posición específica
        self.ramas.pop(posicion)

    def info_arbol(self):   # Devuelve información sobre el árbol
        return f"Tronco: {self.tronco}, Ramas: {len(self.ramas)}, Longitudes de las ramas: {self.ramas}"

arbol = Arbol()     # Crea un árbol
arbol.crecer_tronco()   # Hace crecer el tronco del árbol una unidad 
arbol.nueva_rama()      # Añade una nueva rama al árbol
arbol.crecer_ramas()    # Hace crecer todas las ramas del árbol una unidad    
arbol.nueva_rama()    # Añade una nueva rama al árbol
arbol.nueva_rama()  # Añade una nueva rama al árbol
arbol.quitar_rama(2)    # Retira la rama situada en la posición 2 
print(arbol.info_arbol())   # Obtiene información sobre el árbol

# 36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
# corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
# agregar dinero al saldo.
# Código a seguir:
# 1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
# 2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no
# poder hacerse.
# 3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual.
# Lanzará un error en caso de no poder hacerse.
# 4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
# Caso de uso:
# 1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
# 2. Agregar 20 unidades de saldo de "Bob".
# 3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
# 4. Retirar 50 unidades de saldo a "Alicia".

class UsuarioBanco:     # Define la clase UsuarioBanco
    def __init__(self, nombre, saldo, cuenta_corriente):    # Inicializa el usuario
        self.nombre = nombre    # Nombre del usuario
        self.saldo = saldo  # Saldo del usuario
        self.cuenta_corriente = cuenta_corriente    # Si tiene cuenta corriente o no
    def retirar_dinero(self, cantidad):     # Retira dinero del saldo del usuario
        if self.saldo >= cantidad:  # Si el saldo es mayor o igual que la cantidad a retirar 
            self.saldo -= cantidad  # Resta la cantidad al saldo
        else:   
            raise ValueError("No tienes suficiente saldo")  # Lanza un error, si el saldo es menos que la cantidad a retirar
    def transferir_dinero(self, otro_usuario, cantidad):    # Transfiere dinero desde otro usuario al usuario actual
        if self.saldo >= cantidad:   # Si el saldo es mayor o igual que la cantidad a transferir
            self.saldo -= cantidad      # Resta la cantidad al saldo
            otro_usuario.saldo += cantidad   # Añade la cantidad al saldo del otro usuario
        else:
            raise ValueError("No tienes suficiente saldo")  # Lanza un error, si el saldo es menos que la cantidad a transferir
    def agregar_dinero(self, cantidad):     # Añade dinero al saldo del usuario
        self.saldo += cantidad  # Añade la cantidad al saldo

alicia = UsuarioBanco("Alicia", 100, True)  # Crea un usuario Alicia con saldo inicial de 100 y cuenta corriente
bob = UsuarioBanco("Bob", 50, True)     # Crea un usuario Bob con saldo inicial de 50 y cuenta corriente
bob.agregar_dinero(20)  # Añade 20 unidades de saldo a Bob
bob.transferir_dinero(alicia, 80)   # Hace una transferencia de 80 unidades desde Bob a Alicia
alicia.retirar_dinero(50)   # Retira 50 unidades de saldo a Alicia 
print(alicia.saldo)     # Muestra el saldo de Alicia
print(bob.saldo)    # Muestra el saldo de Bob

# 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras ,
# reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
# de la función procesar_texto .
# Código a seguir:
# 1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene
# que devolver un diccionario.
# 2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene
# que devolver el texto con el remplazo de palabras.
# 3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra
# eliminada.
# 4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un
# número de argumentos variable según la opción indicada.
# Caso de uso:
# Comprueba el funcionamiento completo de la función procesar_texto

def contar_palabras(texto):     
    diccionario = {}
    for palabra in texto.split():   # Divide el texto en palabras omitiendo los espacios
        if palabra in diccionario:
            diccionario[palabra] += 1   # Si la palabra está en el diccionario, suma 1
        else:
            diccionario[palabra] = 1    # Si la palabra no está en el diccionario, la añade
    return diccionario  # Devuelve el diccionario

def reemplazar_palabras(texto, palabra_original, palabra_nueva):    # Reemplaza una palabra original por una nueva en un texto
    return texto.replace(palabra_original, palabra_nueva)   

def eliminar_palabra(texto, palabra):   # Elimina una palabra de un texto
    return texto.replace(palabra, "")

def procesar_texto(texto, opcion, *args):   # Procesa un texto según la opción especificada
    if opcion == "contar":
        return contar_palabras(texto)   # Cuenta las palabras del texto si la opción es "contar"
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, *args)    # Reemplaza una palabra por otra si la opción es "reemplazar"
    elif opcion == "eliminar":
        return eliminar_palabra(texto, *args)   # Elimina una palabra si la opción es "eliminar"

texto = "Hola mundo, me llamo Raúl y me gusta el mundo"
print(procesar_texto(texto, "contar"))
print(procesar_texto(texto, "reemplazar", "mundo", "adios"))
print(procesar_texto(texto, "eliminar", "mundo"))


# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

def hora_del_dia():     # Determina si es de noche, de día o tarde según la hora proporcionada por el usuario
    try:    
        hora = int(input("Introduce una hora: "))
        if hora < 0 or hora > 24: 
            raise ValueError    # Lanza una excepción si la hora es menor que 0 o mayor que 24 
        elif hora >= 6 and hora < 12:   
            print("Es por la mañana")   # Si la hora está entre 6 y 12, es por la mañana
        elif hora >= 12 and hora < 20:  # Si la hora está entre 12 y 20, es por la tarde
            print("Es por la tarde")
        else:
            print("Es de noche")   # Si la hora está entre 20 y 6, es de noche  
    except ValueError:
        print("Debes introducir una hora válida")

hora_del_dia()

# 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
# Las reglas de calificación son:
# - 0 - 69 insuficiente
# - 70 - 79 bien
# - 80 - 89 muy bien
# - 90 - 100 excelente

def calificacion_texto():   # Determina qué calificación en texto tiene un alumno en base a su calificación numérica
    try:    # Intenta determinar la calificación en texto
        calificacion = int(input("Introduce una calificación: "))
        if calificacion < 0 or calificacion > 100:
            raise ValueError    
        elif calificacion < 70:
            print("Insuficiente")  # Si la calificación es menor que 70, es insuficiente
        elif calificacion < 80:
            print("Bien")  # Si la calificación es menor que 80, es bien  
        elif calificacion < 90:
            print("Muy bien") # Si la calificación es menor que 90, es muy bien
        else:
            print("Excelente") # Si la calificación es menor que 100 y mayor que 90, es excelente
    except ValueError:
        print("Debes introducir una calificación válida")

calificacion_texto()

# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o
# "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).

def area_figura(figura, datos):     # Calcula el área de una figura
    if figura == "rectangulo":
        return datos[0] * datos[1]  
    elif figura == "circulo":
        return 3.14 * datos[0] ** 2     # Calcula el área del círculo
    elif figura == "triangulo":
        return (datos[0] * datos[1]) / 2    # Calcula el área del triángulo

print(area_figura("rectangulo", (5, 10)))
print(area_figura("circulo", (5,)))
print(area_figura("triangulo", (5, 10)))

# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
# monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo
# siguiente:
# 1. Solicita al usuario que ingrese el precio original de un artículo.
# 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
# 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
# 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor
# a cero). Por ejemplo, descuento de 15€.
# 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
# 6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu
# programa de Python.

def calcular_monto_final():     # Calcula el monto final de una compra en una tienda en línea
    try:    # Intenta calcular el monto final
        precio_original = float(input("Introduce el precio original del artículo: "))   # Pide al usuario introducir el precio original del artículo
        tiene_cupon = input("¿Tienes un cupón de descuento? (sí o no): ").strip().lower()   # Elimina los espacios y convierte a minúsculas
        
        if tiene_cupon == "sí" or tiene_cupon == "si":   # Si el usuario ha escrito sí con tilde o sin tilde, tiene un cupón de descuento
            valor_cupon = float(input("Introduce el valor del cupón de descuento: "))   # Pide al usuario introducir el valor del cupón de descuento
            if valor_cupon > 0:
                precio_final = precio_original - valor_cupon  # Resta el valor del cupón al precio original
            else:
                print("El valor del cupón no es válido. No se aplicará descuento.")
                precio_final = precio_original  # Si el valor del cupón no es válido, no se aplica descuento
        else:
            precio_final = precio_original  # Si el usuario no tiene un cupón de descuento, el precio final es el precio original
        
        print(f"El precio final de la compra es: {precio_final:.2f}€")
    
    except ValueError:
        print("Por favor, introduce un valor numérico válido.")    # Mensaje que se muestra si el usuario introduce un valor no numérico

calcular_monto_final()


