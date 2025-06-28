import pygame, config
import pantallas,palabras
from assets import personaje, moneda

# pygame.quit() # Cierro el pygame para usarlo solo cuando sea necesario en las pruebas

# ================== Funciones solo para testing ==================
def inicializar_pygame(prueba):
    pygame.init()
    config.VENTANA = pygame.display.set_mode((config.ANCHO, config.ALTO))
    pygame.display.set_caption(f"Prueba: {prueba}")

# ================== Pruebas de palabras.py ==================
def prueba_cargar_palabras():
    print("### Inicio de prueba_cargar_palabras ###")
    palabras_cargadas = None
    try:
        palabras_cargadas = palabras.cargar_palabras()
        print("Sin errores al cargar palabras de un archivo")
    except IOError:
        print("Error: Problema al leer el archivo")
        print("### Fin de prueba_cargar_palabras ###")
        return
    
    try:
        if any([palabra.strip() != palabra for palabra in palabras_cargadas]):
            print("Error: Las palabras incluyen saltos de linea o espacios")
    except TypeError:
        print("Error: Las palabras no estan cargando")
    print("### Fin de prueba_cargar_palabras ###\n")

def prueba_elegir_palabra():
    print("### Inicio de prueba_elegir_palabra ###")
    palabras_cargadas = palabras.cargar_palabras()

    print("Se imprimiran 10 palabras aleatorias. Verificar que sean aleatorias.")
    for x in range(10): print(palabras.elegir_palabra(palabras_cargadas))
    print("### Fin de prueba_elegir_palabra ###\n")

def prueba_verificar_letra():
    print("### Inicio de prueba_verificar_letra ###")
    palabra = "FOOBAR"
    letras_adivinadas = []
    letra_incluida = "O"
    letra_no_incluida = "K"

    len_adivinadas_anterior = len(letras_adivinadas)

    if not palabras.verificar_letra(letra_incluida,palabra,letras_adivinadas):
        print("Error: Una letra valida no se valido")
    if not len(letras_adivinadas) > len_adivinadas_anterior:
        print("Error: No se estan sumando las letras adivinadas a la lista")
    len_adivinadas_anterior = len(letras_adivinadas)

    if palabras.verificar_letra(letra_no_incluida,palabra,letras_adivinadas):
        print("Error: Una letra invalida fue verificada como correcta")
    if not len(letras_adivinadas) > len_adivinadas_anterior:
        print("Error: No se estan sumando las letras adivinadas a la lista")

    palabras.verificar_letra(letra_no_incluida,palabra,letras_adivinadas)
    if not len(letras_adivinadas) == len_adivinadas_anterior:
        print("Error: Se estan sumando letras repetidas a la lista de adivinadas")

    print("### Fin de prueba_verificar_letra ###\n")

def prueba_verificar_final():
    print("### Inicio de prueba_verificar_final ###")
    
    if palabras.verificar_final("FOOBAR", [], 0):
        print("Error: Juego termino antes de tiempo")
    if not palabras.verificar_final("FOOBAR", ["Q","L","K","Ñ","Z","X"], 6):
        print("Error: Juego deberia haber terminado por errores")
    if not palabras.verificar_final("FOOBAR", ["F","O","B","A","L","K","Ñ","Z","X"], 6):
        print("Error: Juego deberia haber terminado por errores")
    if not palabras.verificar_final("FOOBAR", ["F","O","B","A","R"], 0):
        print("Error: Juego deberia haber terminado por adivinar todas las letras")
    if palabras.verificar_final("FOOBAR", ["Q","L","F","O","B","A","R"], 2):
        print("Error: Juego deberia haber terminado por adivinar todas las letras")

    print("### Fin de prueba_verificar_final ###\n")

# ================== Pruebas de pantallas.py ==================

def prueba_dibujar_estructura():
    print("### Inicio de prueba_dibujar_estructura ###")
    inicializar_pygame("prueba_dibujar_estructura")
    print("Verifica en la ventana si la estructura se dibuja de forma correcta")

    reloj = pygame.time.Clock()
    probar = True
    while probar:
        eventos = pygame.event.get()
        for evento in eventos:
            
            match evento.type:
                case pygame.QUIT:
                    probar = False
        
        config.VENTANA.fill(config.NEGRO)
        pantallas.dibujar_estructura()

        pygame.display.flip() # flip() actualiza el contenido de toda la pantalla.
        reloj.tick(30) # Limita los fps a 30.

    pygame.quit()
    print("### Fin de prueba_dibujar_estructura ###\n")

def prueba_dibujar_cuerpo():
    print("### Inicio de prueba_dibujar_cuerpo ###")
    inicializar_pygame("prueba_dibujar_cuerpo")

    print("Verifica en la ventana si se dibuja el cuerpo de forma correcta. Presiona la barra espaciadora para agregar errores")

    reloj = pygame.time.Clock()
    errores = 0

    for errores in range(7):
        probar = True
        print(f"Viendo dibujo con {errores} errores")
        while probar:
            eventos = pygame.event.get()
            for evento in eventos:
                
                match evento.type:
                    case pygame.QUIT:
                        probar = False
                    case pygame.KEYDOWN:
                        probar = False
            
            config.VENTANA.fill(config.NEGRO)
            pantallas.dibujar_cuerpo(errores)

            pygame.display.flip() # flip() actualiza el contenido de toda la pantalla.
            reloj.tick(30) # Limita los fps a 30.

    pygame.quit()
    print("### Fin de prueba_dibujar_cuerpo ###\n")

def prueba_dibujar_juego():
    print("### Inicio de prueba_dibujar_juego ###")
    inicializar_pygame("prueba_dibujar_juego")

    print("Verifica en la ventana si se dibuja el juego de forma correcta")

    reloj = pygame.time.Clock()
    probar = True

    while probar:
        eventos = pygame.event.get()
        for evento in eventos:
            
            match evento.type:
                case pygame.QUIT:
                    probar = False
        
        config.VENTANA.fill(config.NEGRO)
        pantallas.dibujar_juego("FOOBAR",["F","B","R","Q","T","L"],3)

        pygame.display.flip() # flip() actualiza el contenido de toda la pantalla.
        reloj.tick(30) # Limita los fps a 30.

    pygame.quit()
    print("### Fin de prueba_dibujar_juego ###\n")

def prueba_dibujar_victoria():
    print("### Inicio de dibujar_victoria ###")
    inicializar_pygame("dibujar_victoria")

    print("Verifica en la ventana si se dibuja la victoria de forma correcta")

    reloj = pygame.time.Clock()
    probar = True

    while probar:
        eventos = pygame.event.get()
        for evento in eventos:
            
            match evento.type:
                case pygame.QUIT:
                    probar = False
        
        config.VENTANA.fill(config.NEGRO)
        pantallas.dibujar_victoria("FOOBAR",["F","O","B","A","R","Q","T","L"])

        pygame.display.flip() # flip() actualiza el contenido de toda la pantalla.
        reloj.tick(30) # Limita los fps a 30.

    pygame.quit()
    print("### Fin de dibujar_victoria ###\n")

def prueba_dibujar_derrota():
    print("### Inicio de prueba_dibujar_derrota ###")
    inicializar_pygame("prueba_dibujar_derrota")

    print("Verifica en la ventana si se dibuja la derrota de forma correcta")

    reloj = pygame.time.Clock()
    probar = True

    while probar:
        eventos = pygame.event.get()
        for evento in eventos:
            
            match evento.type:
                case pygame.QUIT:
                    probar = False
        
        config.VENTANA.fill(config.NEGRO)
        pantallas.dibujar_derrota("FOOBAR", ["F","O","B","A","L","K","Ñ","Z","X"])

        pygame.display.flip() # flip() actualiza el contenido de toda la pantalla.
        reloj.tick(30) # Limita los fps a 30.

    pygame.quit()
    print("### Fin de prueba_dibujar_derrota ###\n")

# ================== Pruebas de personaje.py ==================
# El personaje es practicamente un juego independiente,
# asi que tiene una sola prueba para probar si funciona
def prueba_personaje():
    print("### Inicio de prueba de personaje ###")
    inicializar_pygame("prueba de personaje")

    print("Verifica si el personaje se comporta correctamente")
    personaje.init()
    moneda.init()

    pj = personaje.procesar_personaje() # Procesamos el personaje para obtener su rectangulo de ubicacion
    coin = moneda.crear_monedas() # Creamos las ubicaciones de las monedas

    reloj = pygame.time.Clock()
    probar = True

    while probar:
        eventos = pygame.event.get()
        for evento in eventos:
            match evento.type:
                case pygame.QUIT:
                    probar = False
        
        config.VENTANA.fill(config.NEGRO)
        """Funciones del pj y la moneda"""
        personaje.procesar_evento(pj) #Funcion para que el personaje se mueva
        personaje.dibujar_personaje(pj) # Dibujamos el personaje
        personaje.colision_personaje(pj, coin)

        moneda.dibujar_monedas(coin)
        "------------------------------"

        pygame.display.flip() # flip() actualiza el contenido de toda la pantalla.
        reloj.tick(30) # Limita los fps a 30.

    pygame.quit()
    print("### Fin de prueba de personaje ###\n")

if __name__ == "__main__":
    # Pruebas de palabras.py
    # prueba_cargar_palabras()
    # prueba_elegir_palabra()
    # prueba_verificar_letra()
    # prueba_verificar_final()

    # Pruebas de pantallas.py
    # prueba_dibujar_estructura()
    # prueba_dibujar_cuerpo()
    # prueba_dibujar_juego()
    # prueba_dibujar_victoria()
    # prueba_dibujar_derrota()

    # Pruebas de personaje.py
    #prueba_personaje()
    pass