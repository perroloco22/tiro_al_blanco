import pygame
import sys
from target import Target
from crosshair import Crosshair
from constantes import *



# Configuración general del juego
pygame.init()

font_titulo = pygame.font.Font('Halimount.otf', TEXT_HEIGHT)
txt_titulo = font_titulo.render("Puntaje: 0", True, "white",'black')



clock = pygame.time.Clock()

# Configuración de la pantalla del juego
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Fondo del juego
# Carga la imagen de fondo desde un archivo
background = pygame.image.load('BG.png')
pygame.mouse.set_visible(False)  # Oculta el cursor del mouse

# Mira del jugador
crosshair = Crosshair('crosshair.png')  # Crea una instancia de la mira
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)  # Agrega la mira al grupo

# Objetivos
target_group = Target.Cargar_target_group()

crosshair.Set_target_group(target_group)
repeat = 1
bandera = True

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Sale del juego si se cierra la ventana
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()  # Llama al método shoot() cuando se hace clic
            txt_titulo = font_titulo.render(f'Puntaje: {crosshair.score.Current_score}', True, "white",'black')
    
    
    if len(target_group) == 0 and repeat > 0:
        target_group = Target.Cargar_target_group()
        crosshair.Set_target_group(target_group)
        repeat -= 1
    
    if repeat == 0 and len(target_group) == 0 and bandera:
        print(f'Juego finalizado su puntaje es: {crosshair.score.Current_score}')
        print(f'Acertados: {crosshair.score.Hit}')
        print(f'Errados: {crosshair.score.Fails}')
        bandera = False
    


    pygame.display.flip()  # Actualiza la pantalla
    screen.blit(background, (0, 0))  # Dibuja el fondo en la pantalla
    screen.blit(txt_titulo, (0, 0))

    for target in target_group:
        target.update(FPS)

    target_group.draw(screen)  # Dibuja los objetivos en la pantalla
    crosshair_group.draw(screen)  # Dibuja la mira en la pantalla

    crosshair_group.update()  # Actualiza la posición de la mira
    clock.tick(FPS)  # Controla la velocidad del juego a 60 cuadros por segundo
