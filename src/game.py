import pygame

from const import *
from board import Board
from dragger import Dragger
from square import Square

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
                color = "#FFF2CC" if (move.end.row + move.end.col) % 2 == 0 else "#FFEEBD"
                rect = (move.end.col * SQ_SIZE, move.end.row * SQ_SIZE, SQ_SIZE, SQ_SIZE)
                pygame.draw.rect(surface, color, rect)
                        
    