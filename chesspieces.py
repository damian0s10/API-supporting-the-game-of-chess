from chessboard import Chessboard
from typing import List
from figure import Figure


class King(Figure):
    def list_available_moves(self) -> List[str]:
        chessboard: Chessboard = Chessboard()

        x_index: int = chessboard.x_size.index(self.field[0])
        y_index: int = chessboard.y_size.index(self.field[1])

        """ Can move one square in every direction """
        for x_field in range(x_index - 1, x_index + 2):

            for y_field in range(y_index - 1, y_index + 2):

                if (
                    (x_index != x_field or y_index != y_field)
                    and (x_field != -1 and y_field != -1)
                    and (x_field != 8 and y_field != 8)
                ):

                    move: str = chessboard.x_size[x_field] + chessboard.y_size[y_field]
                    self.available_moves.append(move)

        return self.available_moves


class Queen(Figure):
    def list_available_moves(self) -> List[str]:
        chessboard: Chessboard = Chessboard()

        x_index: int = chessboard.x_size.index(self.field[0])
        y_index: int = chessboard.y_size.index(self.field[1])

        """ Movement horizontally """
        for x_field in chessboard.x_size:
            if x_field != self.field[0]:
                self.available_moves.append(x_field + self.field[1])

        """ Movement vertically """
        for y_field in chessboard.y_size:
            if y_field != self.field[1]:
                self.available_moves.append(self.field[0] + y_field)

        move: str

        """ Direction right-up """
        for i in range(1, 8 - max(x_index, y_index)):
            move = chessboard.x_size[x_index + i] + chessboard.y_size[y_index + i]
            self.available_moves.append(move)

        """ Direction left-bottom """
        for i in range(1, min(x_index, y_index) + 1):
            move = chessboard.x_size[x_index - i] + chessboard.y_size[y_index - i]
            self.available_moves.append(move)

        """ Direction right-bottom """
        for i in range(1, min(7 - x_index, y_index) + 1):
            move = chessboard.x_size[x_index + i] + chessboard.y_size[y_index - i]
            self.available_moves.append(move)

        """ Direction left-up """
        for i in range(1, min(x_index, 7 - y_index) + 1):
            move = chessboard.x_size[x_index - i] + chessboard.y_size[y_index + i]
            self.available_moves.append(move)

        return self.available_moves


class Rook(Figure):
    def list_available_moves(self) -> List[str]:
        chessboard: Chessboard = Chessboard()

        """ Movement horizontally """
        for x_field in chessboard.x_size:
            if x_field != self.field[0]:
                self.available_moves.append(x_field + self.field[1])

        """ Movement vertically """
        for y_field in chessboard.y_size:
            if y_field != self.field[1]:
                self.available_moves.append(self.field[0] + y_field)

        return self.available_moves


class Bishop(Figure):
    def list_available_moves(self) -> List[str]:
        chessboard: Chessboard = Chessboard()

        x_index: int = chessboard.x_size.index(self.field[0])
        y_index: int = chessboard.y_size.index(self.field[1])

        move: str

        """ Direction right-up """
        for i in range(1, 8 - max(x_index, y_index)):
            move = chessboard.x_size[x_index + i] + chessboard.y_size[y_index + i]
            self.available_moves.append(move)

        """ Direction left-bottom """
        for i in range(1, min(x_index, y_index) + 1):
            move = chessboard.x_size[x_index - i] + chessboard.y_size[y_index - i]
            self.available_moves.append(move)

        """ Direction right-bottom """
        for i in range(1, min(7 - x_index, y_index) + 1):
            move = chessboard.x_size[x_index + i] + chessboard.y_size[y_index - i]
            self.available_moves.append(move)

        """ Direction left-up """
        for i in range(1, min(x_index, 7 - y_index) + 1):
            move = chessboard.x_size[x_index - i] + chessboard.y_size[y_index + i]
            self.available_moves.append(move)

        return self.available_moves


class Knight(Figure):
    def list_available_moves(self) -> List[str]:
        chessboard: Chessboard = Chessboard()

        x_index: int = chessboard.x_size.index(self.field[0])
        y_index: int = chessboard.y_size.index(self.field[1])

        move: str

        """ Direction up """
        if y_index < 6:
            if x_index != 0:
                move = chessboard.x_size[x_index - 1] + chessboard.y_size[y_index + 2]
                self.available_moves.append(move)
            if x_index != 7:
                move = chessboard.x_size[x_index + 1] + chessboard.y_size[y_index + 2]
                self.available_moves.append(move)

        """ Direction bottom """
        if y_index > 1:
            if x_index != 0:
                move = chessboard.x_size[x_index - 1] + chessboard.y_size[y_index - 2]
                self.available_moves.append(move)
            if x_index != 7:
                move = chessboard.x_size[x_index + 1] + chessboard.y_size[y_index - 2]
                self.available_moves.append(move)

        """ Direction right """
        if x_index < 6:
            if y_index != 0:
                move = chessboard.x_size[x_index + 2] + chessboard.y_size[y_index - 1]
                self.available_moves.append(move)
            if y_index != 7:
                move = chessboard.x_size[x_index + 2] + chessboard.y_size[y_index + 1]
                self.available_moves.append(move)

        """ Direction left """
        if x_index > 1:
            if y_index != 0:
                move = chessboard.x_size[x_index - 2] + chessboard.y_size[y_index - 1]
                self.available_moves.append(move)
            if y_index != 7:
                move = chessboard.x_size[x_index - 2] + chessboard.y_size[y_index + 1]
                self.available_moves.append(move)

        return self.available_moves


class Pawn(Figure):
    """ It was assumed that the pawn was started at the bottom of the board """

    def list_available_moves(self) -> List[str]:
        chessboard: Chessboard = Chessboard()

        """ Can move forward one square """
        short_move: str = self.field[0] + str(int(self.field[1]) + 1)
        if chessboard.validate_field(short_move):
            self.available_moves.append(short_move)

        """ Pawn can move forward two squares at the beginning """
        if int(self.field[1]) == 2:
            long_move: str = self.field[0] + str(int(self.field[1]) + 2)
            if chessboard.validate_field(long_move):
                self.available_moves.append(long_move)

        return self.available_moves
