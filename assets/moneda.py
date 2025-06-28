import pygame
from config import VENTANA, ANCHO, ALTO
MONEDA = {} # Diccionario para almacenar las propiedades de la moneda
def init():
    MONEDA.update({  # Velocidad de movimiento horizontal
        "ancho": 50,  # Ancho del obstáculo
        "alto": 50,  # Alto del obstáculo
        "imagen": pygame.image.load("assets/img/moneda_g.png"),  # Carga la imagen del obstáculo
        "posiciones": []  # Lista para almacenar las posiciones de los obstáculos
    })
    MONEDA["imagen"] = pygame.transform.scale(MONEDA["imagen"], (MONEDA["ancho"], MONEDA["alto"])) # Escala la imagen de la moneda al tamaño especificado

def crear_monedas(): # Crea una lista de rectángulos que representan las posiciones de las monedas
    ubicaciones = [((ANCHO / 2) - 200, ALTO - (ALTO / 3) + 100),
                   ((ANCHO / 2) + 100, ALTO - (ALTO / 3) + 54), 
                   ((ANCHO / 2) - 350, ALTO - (ALTO / 3) + 40),
                   ((ANCHO / 2) + 190, ALTO - (ALTO / 3) + 100), 
                   ((ANCHO / 2) - 80, ALTO - (ALTO / 3) + 110), 
                   ((ANCHO / 2) + 300, ALTO - (ALTO / 3) + 120)] # Lista de ubicaciones donde se generarán las monedas
    for x, y in ubicaciones:
        obj = pygame.Rect(int(x), int(y), MONEDA["ancho"], MONEDA["alto"]) # Crea un rectángulo en la posición especificada
        MONEDA["posiciones"].append(obj) # Añade el rectángulo a la lista de posiciones de las monedas
    return MONEDA["posiciones"] # Devuelve la lista de rectángulos que representan las monedas

def dibujar_monedas(moneda): # Dibuja las monedas en la pantalla
    for coin in moneda:
        if MONEDA["imagen"]:
            VENTANA.blit(MONEDA["imagen"], coin)  # Dibuja la imagen de la moneda en la posición especificada por el rectángulo