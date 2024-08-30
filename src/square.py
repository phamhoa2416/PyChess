class Square:
    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece
        
    def has_piece(self):
        return self.piece is not None
    
    def is_empty(self):
        return self.piece is None
    
    def has_ally(self, color):
        return self.has_piece() and self.piece.color == color
    
    def has_enemy(self, color):
        return self.has_piece() and self.piece.color != color
    
    def is_empty_or_enemy(self, color):
        return self.is_empty() or self.has_enemy(color)
    
    @staticmethod
    def in_range(*args):
        for arg in args:
            if not 0 <= arg < 8:
                return False
        return True
    
    