"""
# Data structures.
/src/structures_detroix23/modules/chain.py
"""
from typing import Optional

import base

class Cell:
    """
    Define a cell from a chained list.
    """
    _value: int
    _following: Optional['Cell']

    def __init__(self, value: int, following: Optional['Cell'] = None) -> None:
        self._value = value
        self._following = following

    def __str__(self) -> str:
        display: list[str] = []
        current: Optional[Cell] = base.copy(self)
        while current is not None:
            display.append(str(current.get_value))
            current = current.get_following

        return f"<[{', '.join(display)}]>"

    def __repr__(self) -> str:
        return f"chain.Cell(value={self.get_value}, following={self.get_following})"

    def __copy__(self) -> 'Cell':
        return Cell(
            value=self.get_value,
            following=self.get_following,
        )

    @property
    def get_value(self) -> int:
        """
        Get the value of the cell.
        """
        return self._value

    @property
    def get_following(self) -> Optional['Cell']:
        """
        Get the next cell. Return None has no following.
        """
        return self._following
    @staticmethod
    def new_from_list(values: list[int]) -> 'Cell':
        """
        Generate a chained list from a given `values` list.
        """
        values.reverse()
        current: Cell = Cell(values[0])
        for value in values[1:]:
            current = Cell(value, current)

        return current

    def go(self, steps: int) -> 'Cell':
        """
        Move up `steps` times, and return the `Cell`.
        Throws an `IndexError` if the index is out of range.
        """
        current: Cell = base.copy(self)
        while steps > 0:
            if current.get_following is None:
                raise IndexError(f"(X) - modules.chain.Cell.go - Index out of range. Remaining steps = {steps}, Cell = {current}")
            current = current.get_following

        return current

def main() -> None:
    """
    Main chained list test entry point.
    """
    print("## Chained lists.")

    c1 = Cell(1)
    print(c1)

    c2 = Cell(1, Cell(2, Cell(3)))
    print(c2)

    c3 = Cell.new_from_list([1, 2, 3, 4])
    print(c3)

    print(f"{c3.go(2)=}")

if __name__ == "__main__":
    main()




