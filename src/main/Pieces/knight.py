from Pieces.piece import Piece
from Game.square import Square
from Game.move import Move
                          
class Knight(Piece):
    def __init__(self, color):  
        super().__init__("knight", color, 3.0)
        
