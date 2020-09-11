from typing import Tuple


class Chessboard:

    x_size: Tuple[str, str, str, str, str, str, str, str] = (
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
    )
    y_size: Tuple[str, str, str, str, str, str, str, str] = (
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
    )

    def validate_field(self, field: str) -> bool:

        if field[0] in self.x_size:
            if field[1:] in self.y_size:
                return True
        return False
