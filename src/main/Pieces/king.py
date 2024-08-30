from Pieces.piece import Piece
        
class King(Piece):
    def __init__(self, color):
        self.left_rook = None
        self.right_rook = None 
        super().__init__("king", color, 1000.0)