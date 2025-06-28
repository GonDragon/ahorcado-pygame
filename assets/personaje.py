import pygame
from config import VENTANA, ANCHO, ALTO, sonido_moneda # Podes importar cualquier variable global de config

PERSONAJE = {} 
def init():
    PERSONAJE.update({
        "velocidad_x": 6,  # Velocidad de movimiento horizontal
        "velocidad_y": 6,  # Velocidad de movimiento vertical
        "ancho": 60,  # Ancho del personaje
        "alto": 60,  # Alto del personaje
        "imagen": pygame.image.load("assets/img/capibara.png")  # Carga la imagen del personaje
    })
    PERSONAJE["imagen"] = pygame.transform.scale(PERSONAJE["imagen"], (PERSONAJE["ancho"], PERSONAJE["alto"]))
# ----------------- Eventos del personaje -----------------
def procesar_evento(personaje):
    # Recibe todos los eventos de pygame.event.get()
    # Asi que lo podes usar para detectar teclas precionadas con evento.type == pygame.KEYDOWN, por ejemplo
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and personaje.left > 0:
        personaje.x -= PERSONAJE["velocidad_x"]
    if teclas[pygame.K_RIGHT] and personaje.right < ANCHO:
        personaje.x += PERSONAJE["velocidad_x"]
    if teclas[pygame.K_UP] and personaje.top > ALTO - (ALTO / 3):
        personaje.y -= PERSONAJE["velocidad_y"]
    if teclas[pygame.K_DOWN] and personaje.bottom < ALTO:
        personaje.y += PERSONAJE["velocidad_y"]

# ----------------- Creando al personaje -----------------
def procesar_personaje():
    x = int(ANCHO - (ANCHO / 2))  # Posición inicial en el centro/derecha de la pantalla
    y = int(ALTO - (ALTO / 5)) # Posición inicial en la parte inferior de la pantalla
    ubicacion = pygame.Rect(x, y, PERSONAJE["ancho"], PERSONAJE["alto"]) # Crea un rectángulo que representa al personaje
    return ubicacion  # Devuelve el rectángulo que representa al personaje

# ----------------- Dibujando al personaje -----------------
def dibujar_personaje(personaje):
    if PERSONAJE["imagen"]: # Verifica si la imagen del personaje está cargada
        VENTANA.blit(PERSONAJE["imagen"], personaje.topleft) # Dibuja la imagen del personaje en la ventana

def colision_personaje(pj ,monedas):
    #Verifica si el personaje colisiona con alguna moneda
    for moneda in monedas: # Recorre la lista de monedas
        # Verifica si el rectángulo del personaje colisiona con el rectángulo de la moneda
        if pj.colliderect(moneda):
            sonido_moneda.play()
            monedas.remove(moneda) # Elimina la moneda de la lista si hay colisión