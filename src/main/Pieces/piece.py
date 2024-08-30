import os

class Piece:
    def __init__(self, name, color, value, texture=None, texture_rect=None):
        self.name = name
        self.color = color
        self.moves = []
        self.moved = False
        value_sign = 1 if color == "white" else -1
        self.value = value * value_sign
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect
    
    def set_texture(self, size = 80):
        self.texture = os.path.join(f"assets/images/imgs-{size}px/{self.color}_{self.name}.png")
        
    def add_moves(self, move):
        self.moves.append(move)

