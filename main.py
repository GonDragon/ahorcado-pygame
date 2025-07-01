# === PROYECTO FINAL - JUEGO DEL AHORCADO EN PYGAME ===
# Importar librerias de uso general
import pygame,sys,time

# Importar config inicializa pygame y nos provee acceso a las variables globales que vamos a usar
import config

# Importamos los otros modulos que vamos a usar
import palabras, pantallas

# Importamos los modulos de los assets que vamos a usar
from minijuego import personaje, moneda
# ----------------- BUCLE PRINCIPAL -----------------
def jugar():
    personaje.init()  # Inicializamos el personaje
    moneda.init()  # Inicializamos la moneda
    lista_palabras = palabras.cargar_palabras() # guarda en la variable las palabras del archivo txt como una lista.
    palabra_ganadora = palabras.elegir_palabra(lista_palabras) # se guarda en la variable una palabra random de la lista de la variable lista_palabras. 

    errores = 0 # Inicializo la variable de errores en cero.
    letras_adivinadas = [] # inicializo la lista de letras adivinadas como una lista vacia.
    letra_actual = None # la letra actual en None.
    termino = False # Inicializo la variable que ejecuta el while en False.

    pj = personaje.procesar_personaje() # Procesamos el personaje para obtener su rectangulo de ubicacion
    coin = moneda.crear_monedas() # Creamos las ubicaciones de las monedas
    reloj = pygame.time.Clock()
    cant_monedas = 0  # Inicializamos la cantidad de monedas recolectadas
    while not termino: # Mientras que termino no sea False se ejecuta el while.
        eventos = pygame.event.get() # guarda en eventos todos los eventos que ocurren en el juego.
        for evento in eventos: # para cada evento en eventos se ejecutará lo siguiente.
            
            match evento.type: # va a machear el evento con los siguiente casos.
                case pygame.QUIT: # si el evento es QUIT: 
                    pygame.quit() # Sale de pygame.
                    sys.exit() # sale del sistema.
                case pygame.KEYDOWN: # en el caso de que se precione un tecla:
                    if evento.unicode.isalpha(): # si el código de la tecla preciona es una letra
                        letra_actual = evento.unicode.upper() # guarda la letra en mayúscula en la variable
                        print(letra_actual) # imprime en la consola la letra.

        if letra_actual:
            verificada = palabras.verificar_letra(letra_actual, palabra_ganadora, letras_adivinadas) # guarda en la variable si la letra ingresada pertenece a la palabra a adivinar.
            if not verificada: # En caso de que no esté:
                config.sonido_error.play() # reproduce el sonido de error.
                errores += 1 # suma en uno la cantidad de errores 

        # Arrancamos a dibujar. Borramos el frame anterior pintando de negro
        config.VENTANA.fill(config.NEGRO)

        """Funciones del pj y la moneda"""
        personaje.procesar_evento(pj) #Funcion para que el personaje se mueva
        personaje.dibujar_personaje(pj) # Dibujamos el personaje
        cant_monedas = personaje.colision_personaje(pj, coin, cant_monedas) # Colision del pj con la moneda

        if cant_monedas == moneda.MONEDA["cantidad"]: # Verifica si agarro todas las monedas
            errores -= 1 # Le resta un error
            cant_monedas += 1 # Se suma uno a la cantidad de monedas asi deja de restarle al error
            
        moneda.dibujar_monedas(coin) # Dibujando la moneda
        pantallas.mostrar_cantidad_monedas(cant_monedas, moneda.MONEDA["cantidad"])
        "------------------------------"
        pantallas.dibujar_juego(palabra_ganadora, letras_adivinadas, errores) # Encima dibujamos el juego del ahorcado

        termino = palabras.verificar_final(palabra_ganadora, letras_adivinadas, errores) # guarda en la variable un valor booleano de si hay que terminar en juego o no.
        letra_actual = None # la letra atual pasa a ser None otra vez.

        pygame.display.flip() # flip() actualiza el contenido de toda la pantalla.
        reloj.tick(30) # Limita los fps a 30.

    # Borramos el ultimo frame del juego
    config.VENTANA.fill(config.NEGRO)

    if errores < config.INTENTOS_MAXIMOS: # si la cantidad de errores es menor a la cantidad de intentos maximos.
        pantallas.dibujar_victoria(palabra_ganadora, letras_adivinadas) # imprime la pantalla de victoria.
    else: # sino
        pantallas.dibujar_derrota(palabra_ganadora, letras_adivinadas) # imprime la pantalla de derrota.

    pygame.display.flip() # flip() actualiza el contenido de toda la pantalla, para que veamos la pantalla final.

    # Dejamos que la pantalla se vea por tres segundos antes de cerrar
    time.sleep(3) # la pantalla espera 3 segundo antes de ejecutar las siguientes lineas del código.
    pygame.quit() # sale de pygame.
    sys.exit() # sale del sistema.

if __name__ == "__main__":
    jugar()
