from abc import ABC, abstractmethod
from typing import List


class Figure(ABC):
    def __init__(self, field: str) -> None:
        self.field = field
        self.available_moves: List[str] = []

    @abstractmethod
    def list_available_moves(self):
        pass

    def validate_move(self, dest_field: str) -> bool:
        if dest_field in self.available_moves:
            return True
        return False
