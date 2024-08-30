import pygame

from Game.const import *
from Game.board import Board
from Game.dragger import Dragger
from Game.square import Square

class Game:
    
    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()
        
    def show_backgroud(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                color = (234, 235, 200) if (row + col) % 2 == 0 else (119, 154, 80)
                rect = (col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE)
                
                pygame.draw.rect(surface, color, rect)
                
    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece
                    
                    if piece is not self.dragger.piece:
                        piece.set_texture(size = 80)
                        img = pygame.image.load(piece.texture)
                        img_center = col * SQ_SIZE + SQ_SIZE // 2, row * SQ_SIZE + SQ_SIZE // 2
                        piece.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.texture_rect)
                        
    def show_moves(self, surface):
        if self.dragger.dragging:
            piece = self.dragger.piece
            
            for move in piece.moves:
                center = (move.end.col * SQ_SIZE + SQ_SIZE // 2, move.end.row * SQ_SIZE + SQ_SIZE // 2)
                pygame.draw.circle(surface, (202, 203, 179), center, SQ_SIZE // 6)
                        
    