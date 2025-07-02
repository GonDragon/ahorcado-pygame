def validar_letra(letra):
    # Función que valida que el parámetro 'letra' sea un string de un solo carácter

    if not isinstance(letra, str):
        # Si 'letra' no es de tipo string, se lanza un ValueError
        raise ValueError("Las letras deben ser strings")
    
    if len(letra) != 1:
        # Si la longitud de 'letra' no es exactamente 1, se lanza un ValueError
        raise ValueError("Las letras deben contener exactamente 1 caracter")

def validar_palabra(palabra):
    # Función que valida que 'palabra' sea un string y contenga solo letras

    if not isinstance(palabra, str):
        # Si 'palabra' no es de tipo string, se lanza un ValueError
        raise ValueError("Las palabras deben ser strings")
    
    if not palabra.isalpha():
        # Si 'palabra' contiene algo que no sea letras (números, espacios, símbolos), se lanza un ValueError
        raise ValueError("Las palabras solo pueden contener letras, no numeros ni espacios")

def validar_lista_palabras(lista_palabras):
    # Función que valida que 'lista_palabras' sea una lista no vacía y que todas sus palabras sean válidas

    if not isinstance(lista_palabras, list):
        # Si 'lista_palabras' no es de tipo lista, se lanza un ValueError
        raise ValueError("La lista de palabras debe ser una lista")
    
    if len(lista_palabras) == 0:
        # Si 'lista_palabras' está vacía, se lanza un ValueError
        raise ValueError("La lista de palabras debe contener elementos")
    
    for palabra in lista_palabras:
        # Recorre cada elemento de la lista y valida que sea una palabra válida
        validar_palabra(palabra)

def validar_lista_letras(lista_letras):
    # Función que valida que 'lista_letras' sea una lista y que todas las letras contenidas sean válidas

    if not isinstance(lista_letras, list):
        # Si 'lista_letras' no es de tipo lista, se lanza un ValueError
        raise ValueError("La lista de palabras debe ser una lista")
    
    for letra in lista_letras:
        # Recorre cada elemento de la lista y valida que sea una letra válida
        validar_letra(letra)

def validar_errores(errores):
    # Función que valida que 'errores' sea un número entero

    if not isinstance(errores, int):
        # Si 'errores' no es un entero, se lanza un ValueError
        raise ValueError("Los errores deben ser numeros enteros")
