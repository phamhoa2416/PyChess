from Pieces.piece import Piece
from Game.square import Square
from Game.move import Move

class Pawn(Piece):
    def __init__(self, color):
        self.direction = -1 if color == "white" else 1
        super().__init__("pawn", color, 1.0)
        
    def pawn_moves(self, piece, row, col):
        # steps
        steps = 1 if piece.moved else 2
            
        # vertical moves
        start_point = row + piece.direction
        end_point = row + piece.direction * (1 + steps)
            
        for possible_move_row in range(start_point, end_point, piece.direction):
            if Square.in_range(possible_move_row):
                if self.squares[possible_move_row][col].is_empty():
                    start = Square(row, col)
                    end = Square(possible_move_row, col)
                    move = Move(start, end)
                    piece.add_moves(move)
                else: break
            else: break
            
        # diagonal moves
        possible_move_row = row + piece.direction
        possible_move_cols = [col - 1, col + 1]
        for possible_move_col in possible_move_cols:
            if Square.in_range(possible_move_row, possible_move_col):
                if self.squares[possible_move_row][possible_move_col].has_enemy(piece.color):
                    start = Square(row, col)
                    end = Square(possible_move_row, possible_move_row)
                    move = Move(start, end)
                    piece.add_moves(move)