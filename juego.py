import pygame

#------Clases-------

class Personaje(pygame.sprite.Sprite):
    def __init__(self):

    def update(self):

    def saltar(self):

    def mov_izquierda(self):

    def mov_derecha(self):

    def stop(self):

class Plataforma(pygame.sprite.Sprite):
    def __init__(self, alto, largo):
        super().__init__()

        self.image = pygame.surface((largo, alto))
        self.image.fill((0,255,0))

        self.rect = self.image.get_rect()

#-----Funciones-------

def main():
    pygame.init()

if __name__ == '__main__':
    main()
