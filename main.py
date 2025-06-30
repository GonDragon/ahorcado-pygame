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
    lista_palabras = palabras.cargar_palabras()
    palabra_ganadora = palabras.elegir_palabra(lista_palabras)
    #palabra_ganadora = "PYTHON"  # Para pruebas, usamos una palabra fija
    errores = 0
    letras_adivinadas = []
    letra_actual = None
    termino = False

    pj = personaje.procesar_personaje() # Procesamos el personaje para obtener su rectangulo de ubicacion
    coin = moneda.crear_monedas() # Creamos las ubicaciones de las monedas
    reloj = pygame.time.Clock()
    cant_monedas = 0  # Inicializamos la cantidad de monedas recolectadas
    while not termino:
        eventos = pygame.event.get()
        for evento in eventos:
            
            match evento.type:
                case pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                case pygame.KEYDOWN:
                    if evento.unicode.isalpha():
                        letra_actual = evento.unicode.upper()
                        print(letra_actual)

        if letra_actual:
            verificada = palabras.verificar_letra(letra_actual, palabra_ganadora, letras_adivinadas)
            if not verificada:
                config.sonido_error.play()
                errores += 1

        # Arrancamos a dibujar. Borramos el frame anterior pintando de negro
        config.VENTANA.fill(config.NEGRO)

        """Funciones del pj y la moneda"""
        personaje.procesar_evento(pj) #Funcion para que el personaje se mueva
        personaje.dibujar_personaje(pj) # Dibujamos el personaje
        cant_monedas = personaje.colision_personaje(pj, coin, cant_monedas) # Colision del pj con la moneda

        moneda.dibujar_monedas(coin) # Dibujando la moneda
        pantallas.mostrar_cantidad_monedas(cant_monedas, moneda.MONEDA["cantidad"])
        "------------------------------"
        pantallas.dibujar_juego(palabra_ganadora, letras_adivinadas, errores) # Encima dibujamos el juego del ahorcado

        termino = palabras.verificar_final(palabra_ganadora, letras_adivinadas, errores)
        letra_actual = None
        
        pygame.display.flip() # flip() actualiza el contenido de toda la pantalla.
        reloj.tick(30) # Limita los fps a 30.

    # Borramos el ultimo frame del juego
    config.VENTANA.fill(config.NEGRO)

    if errores < config.INTENTOS_MAXIMOS:
        pantallas.dibujar_victoria(palabra_ganadora, letras_adivinadas)
    else:
        pantallas.dibujar_derrota(palabra_ganadora, letras_adivinadas)

    pygame.display.flip() # flip() actualiza el contenido de toda la pantalla, para que veamos la pantalla final.

    # Dejamos que la pantalla se vea por tres segundos antes de cerrar
    time.sleep(3)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    jugar()
