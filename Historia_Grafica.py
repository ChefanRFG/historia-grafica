import pygame
import sys
pygame.init()

# Configurar la pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Juego de Toma de Decisiones")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Configurar la fuente
font = pygame.font.Font(None, 36)

# Estados del juego
MENU = 0
DECISION = 1
RESULTADO = 2

# Estado inicial del juego
estado_juego = MENU

# Función para dibujar el menú
def dibujar_menu():
    screen.fill(NEGRO)
    texto = font.render("Presiona ESPACIO para empezar", True, BLANCO)
    screen.blit(texto, (200, 300))

def dibujar_menu():
    screen.fill(image = pygame.image.load("inicio1.png"))
    texto = font.render("Apareces en una cueva solitaria...", True, BLANCO)
    screen.blit(texto, (200, 300))

# Función para dibujar las decisiones
def dibujar_decision():
    screen.fill(NEGRO)
    opcion1 = font.render("1. Ir a la ciudad", True, BLANCO)
    opcion2 = font.render("2. Ir al bosque", True, BLANCO)
    screen.blit(opcion1, (100, 200))
    screen.blit(opcion2, (100, 300))

# Función para dibujar el resultado
def dibujar_resultado(resultado):
    screen.fill(NEGRO)
    texto = font.render(resultado, True, BLANCO)
    screen.blit(texto, (200, 300))

# Bucle principal del juego
corriendo = True
while corriendo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            corriendo = False
        elif event.type == pygame.KEYDOWN:
            if estado_juego == MENU:
                if event.key == pygame.K_SPACE:
                    estado_juego = DECISION
            elif estado_juego == DECISION:
                if event.key == pygame.K_1:
                    resultado = "Fuiste a la ciudad y encontraste una aventura!"
                    estado_juego = RESULTADO
                elif event.key == pygame.K_2:
                    resultado = "Fuiste al bosque y encontraste un tesoro!"
                    estado_juego = RESULTADO
            elif estado_juego == RESULTADO:
                if event.key == pygame.K_SPACE:
                    estado_juego = MENU

    # Dibujar según el estado del juego
    if estado_juego == MENU:
        dibujar_menu()
    elif estado_juego == DECISION:
        dibujar_decision()
    elif estado_juego == RESULTADO:
        dibujar_resultado(resultado)

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
sys.exit()
