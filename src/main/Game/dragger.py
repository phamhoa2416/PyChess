import pygame

from Game.const import *

class Dragger:
    def __init__(self):
        self.piece = None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.start_row = 0
        self.start_col = 0
        
    def update_blit(self, surface):
        self.piece.set_texture(80)
        
        img = pygame.image.load(self.piece.texture)
        img_center = (self.mouseX, self.mouseY)
        self.piece.texture_rect = img.get_rect(center=img_center)
        surface.blit(img, self.piece.texture_rect)
        
    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos
        
    def save_position(self, pos):
        self.start_row = pos[1] // SQ_SIZE
        self.start_col = pos[0] // SQ_SIZE
        
    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True
        
    def drop_piece(self):
        self.piece = None
        self.dragging = False