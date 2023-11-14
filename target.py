import pygame
import random
from constantes import *
import pygame
points = [1000, 500, 100]
scales = [(50,50),(95,95)]




class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y, size: int, speed_move: int):
        super().__init__()

        # Carga la imagen del objetivo desde un archivo
        self.size = size
        self.points = points[size]

        self.image = self.__Resize(picture_path)
        self.rect = self.image.get_rect()  # Obtiene el rectángulo que rodea la imagen

        # Establece la posición inicial del objetivo
        self.rect.x = SCREEN_WIDTH - self.image.get_width() if pos_x > SCREEN_WIDTH - self.image.get_width() else pos_x
        self.rect.y = SCREEN_HEIGHT - self.image.get_height() if pos_y > SCREEN_HEIGHT - self.image.get_height() else pos_y
        
        self.player_move_time = 0
        self.frame_rate = 100

        #velocidad de movimiento
        self.speed_move = speed_move
        self.move_right = True
        self.move_down = True


        
    
    @property
    def Points(self)->int:
        return self.points
    
    def __Resize(self,picture_path) -> pygame.Surface:
        image = pygame.image.load(picture_path)
        if self.size != 2:                
            if self.size == 0:
                image = pygame.transform.scale(image,scales[0])
            else:
                image = pygame.transform.scale(image,scales[1])      
        return image

    def __borders_limit(self):

        if self.rect.x > SCREEN_WIDTH - self.image.get_width() or self.rect.x <= 0:
            self.move_right = not self.move_right           
        

        if self.rect.y > SCREEN_HEIGHT - self.image.get_height() or self.rect.y <= TEXT_HEIGHT + 20:
            self.move_down = not self.move_down
   
    def __do_movement(self,delta_ms):
        self.player_move_time += delta_ms

        if self.player_move_time >= self.frame_rate:
            self.player_move_time = 0   
            if self.move_right:
                self.rect.x += self.speed_move
            else:
                self.rect.x -= self.speed_move
            
            if self.move_down:
                self.rect.y += self.speed_move
            else:
                self.rect.y -= self.speed_move

            self.__borders_limit()

    @staticmethod
    def Cargar_target_group():
        target_group = pygame.sprite.Group()
        for _ in range(10):
            new_target = Target('target.png', random.randrange(0, SCREEN_WIDTH), random.randrange(TEXT_HEIGHT + 20, SCREEN_HEIGHT),random.randrange(0,3),speed_move=10)
            target_group.add(new_target)  # Agrega objetivos al grupo
        return target_group
    
    
    def update(self,delta):
        self.__do_movement(delta)
    