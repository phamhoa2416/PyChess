import pygame
import sys

from Game.const import *
from Game.game import Game

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Let's Play Chess!")
        self.game = Game()
        
    def mainloop(self):
        game = self.game
        screen = self.screen
        board = self.game.board
        dragger = self.game.dragger
                
        running = True   
        while running:
            game.show_backgroud(screen)
            game.show_moves(screen)
            game.show_pieces(screen)
            
            if dragger.dragging:
                dragger.update_blit(screen)           
            
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(pygame.mouse.get_pos())
                    
                    row_clicked = dragger.mouseY // SQ_SIZE
                    col_clicked = dragger.mouseX // SQ_SIZE
                    
                    if board.squares[row_clicked][col_clicked].has_piece():
                        piece = board.squares[row_clicked][col_clicked].piece
                        board.calc_moves(piece, row_clicked, col_clicked)
                        dragger.save_position(pygame.mouse.get_pos())
                        dragger.drag_piece(piece)
                        
                        game.show_backgroud(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(pygame.mouse.get_pos())
                        game.show_backgroud(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        dragger.update_blit(screen)
                        
                elif event.type == pygame.MOUSEBUTTONUP:
                    dragger.drop_piece()
                    
                elif event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                    
            pygame.display.update()
                    
main = Main()
main.mainloop()