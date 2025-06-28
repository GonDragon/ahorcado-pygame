import pygame, os

pygame.init()

# ----------------- CONFIGURACIÓN DE PANTALLA -----------------
ANCHO = 800
ALTO = 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
#completar con nombre del equipo
pygame.display.set_caption("Juego del Ahorcado: G-Team Edition")

# ----------------- COLORES  se pueden modificar por los que elija el equipo-----------------
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)

# ----------------- FUENTE -----------------
FUENTE = pygame.font.SysFont(None, 48)

# ----------------- SONIDO -----------------
pygame.mixer.init()  # Inicializa el motor de sonido
sonido_error = pygame.mixer.Sound(os.path.join(os.getcwd(), "recursos","error.wav"))  # Asegurate de tener este archivo

# ------------------ CONFIGURACIONES DE JUEGO -------------------
INTENTOS_MAXIMOS = 6