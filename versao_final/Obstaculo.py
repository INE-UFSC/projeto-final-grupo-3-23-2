from Personagem import Personagem
from Arma import Arma
import random, pygame

class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, nome: str, vidas: int, x: int, y: int, velocidade: int, image:str, sprites):
        self.__nome = nome
        self.__vidas = vidas
        self.__velocidade = velocidade
        self.__image = image
        self.__sprites = sprites
        self.__x = x
        self.__y = y
        self.__maximo_vidas = vidas
        self.__rect = None
    
    def mover_baixo(self):
        self.__y += self.__velocidade

    def mover(self):
        self.mover_baixo()
        """# Determinar a direção para o jogador
        if self.x < jogador_x:
            self.x += 1
        elif self.x > jogador_x:
            self.x -= 1

        if self.y < jogador_y:
            self.y += 1
        elif self.y > jogador_y:
            self.y -= 1
        
        # Garantir que o inimigo não saia da tela
        self.x = max(0, min(self.x, 1050))
        self.y = max(0, min(self.y, 700))"""

    def respawn(self, largura, altura=None):
        self.posicao_aleatoria(largura, altura)
        self.vidas = self.__maximo_vidas

    def posicao_aleatoria(self, largura, altura = None):
        if altura == None:
            self.y = -100
        else:
            self.y = random.randint(altura, 0)
        self.x = random.randint(1, largura-40)

    @property
    def rect(self):
        return self.__rect
    
    @rect.setter
    def rect(self, rect):
        self.__rect = rect

    @property
    def sprites(self):
        return self.__sprites
    
    @sprites.setter
    def sprites(self, sprites):
        self.__sprites = sprites
    
    @property
    def image(self):
        return self.__image
    
    @image.setter
    def image(self, image):
        self.__image = image
    
    @property
    def velocidade(self):
        return self.__velocidade
    
    @velocidade.setter
    def velocidade(self, velocidade):
        self.__velocidade = velocidade
    
    @property
    def vidas(self):
        return self.__vidas
    
    @vidas.setter
    def vidas(self, vidas):
        self.__vidas = vidas
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y):
        self.__y = y