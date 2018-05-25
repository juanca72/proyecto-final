import pygame

#------Clases-------

class Personaje(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()

        alto=50
        ancho=30

        self.image=pygame.surface((alto,ancho))
        self.image.fill((255,0,0))
        self.rect=self.image.get_rect()
        self.velocidad=[0,0]

    def update(self):

    def saltar(self):

    def mov_izquierda(self):
        self.velocidad= -2

    def mov_derecha(self):
        self.velocidad= 2

    def stop(self):
        self.velocidad = 0

class Plataforma(pygame.sprite.Sprite):
    def __init__(self):

#-----Funciones-------

def main():
    pygame.init()

if __name__ == '__main__':
    main()
