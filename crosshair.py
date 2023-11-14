import pygame
from puntaje import Score

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        # Carga la imagen de la mira desde un archivo
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()  # Obtiene el rectángulo que rodea la imagen
        # Carga el sonido de disparo desde un archivo
        self.gunshot = pygame.mixer.Sound('shoot.mp3')

        self.target_group = None
        self.score = Score()

    def Set_target_group(self,target):
        self.target_group = target
        

    def shoot(self):

        self.gunshot.play()  # Reproduce el sonido de disparo
        # Elimina los objetivos que se tocan
        sprites_deleted = pygame.sprite.spritecollide(self, self.target_group, True)
        
        if sprites_deleted:
            for sprite in sprites_deleted:
                self.score.Add_hit(1)
                self.score.Add_points(sprite.Points)
        else:
            self.score.Add_fail(1)
 
    def update(self):
        # Actualiza la posición de la mira para seguir el cursor del mouse
        self.rect.center = pygame.mouse.get_pos()
    
    
    def longitud_actual(self):
        return len(self.target_group)

    


