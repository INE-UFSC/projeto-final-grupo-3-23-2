import pygame
from EstadoGenerico import EstadoGenerico

class EstadoRanking(EstadoGenerico):
    def lidar_com_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                self.jogo.mudar_estado(self.jogo.estado_menu)

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if self.jogo.rect_voltar.collidepoint(evento.pos):
                    self.jogo.mudar_estado(self.jogo.estado_menu)

    def atualizar(self):
        pass

    def desenhar(self):
        self.font = pygame.font.Font('versao_final/assets/fonts/PixelGameFont.ttf', 36)
        # Criando o texto que será exibido na tela, divido por linhas
        
        linhas = [
            "1 - Cid: 1000 pontos",
            "2 - Guilherme: 723 pontos",
            "3 - Henrique: 425 pontos",
        ]

        # Renderizando as linhas de texto
        self.textos = [self.font.render(linha, True, self.jogo.cor) for linha in linhas]

        # Calculando as posições verticais dos textos
        self.rect_textos = [texto.get_rect(center=(1100 // 2, ((660 // 2)-100) + i * 40)) for i, texto in enumerate(self.textos)]
       
        # Desenha os planos de fundo
        self.jogo.screen.blit(self.jogo.bg3, (0, self.jogo.bg3_y))
        self.jogo.screen.blit(self.jogo.bg4, (0, self.jogo.bg4_y))

        pygame.draw.rect(self.jogo.screen, (0, 0, 0), self.jogo.rect_voltar, 2)
        self.jogo.screen.blit(self.jogo.texto_voltar, self.jogo.rect_voltar)

        # Desenhando os textos na tela
        for i, texto in enumerate(self.textos):
            self.jogo.screen.blit(texto, self.rect_textos[i])