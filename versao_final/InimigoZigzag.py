from Inimigo import Inimigo
from Arma import Arma
import random, pygame

class InimigoZigzag(Inimigo):
    def __init__(self, nome: str, vidas: int, x: int, y: int, arma: Arma, velocidade: int, image:str):
        super().__init__(nome, vidas, x, y, arma, velocidade, image)
        self.__direcao_x = 1

    def mover(self):
        self.y += self.velocidade

        # Alteração na direção gradual do movimento
        chance_mudanca_direcao = random.randint(0, 1000)
        if chance_mudanca_direcao < 5:  # Ajuste o valor para mudar a frequência da mudança
            self.__direcao_x *= -1  # Inverte a direção

        self.x += self.velocidade * self.__direcao_x  # Multiplica pela direção

        # Limita a posição do inimigo dentro dos limites da tela
        # Substitua os valores de largura e altura pelos valores corretos da sua tela
        # (largura e altura da tela ou área de jogo)
        if self.x <= 0:
            self.x = 0
            self.__direcao_x *= -1  # Inverte a direção ao atingir o limite esquerdo
        elif self.x >= 1000:
            self.x = 1000
            self.__direcao_x *= -1  # Inverte a direção ao atingir o limite direito
