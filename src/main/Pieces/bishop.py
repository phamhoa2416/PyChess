from Pieces.piece import Piece

class Bishop(Piece):
    def __init__(self, color):  
        super().__init__("bishop", color, 3.0001)