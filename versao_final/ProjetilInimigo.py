from Projetil import Projetil
from Arma import Arma
import random, pygame

class ProjetilInimigo(Projetil):
    def __init__(self, x: int, y: int, velocidade: int, dano: int, sprites):
        super().__init__(x, y, velocidade, dano, sprites)
        self.image = pygame.image.load("versao_final/assets/imgs/shot4_5.png")
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect(center = (x, y))

    def update(self, largura):
        # Movimentar o projétil
        if self.y >= largura:
            self.kill()
        else:
            self.rect.y += self.velocidade