"""
# Data structures.
/src/structures_detroix23/modules/chain.py
"""

from typing import Optional, TypeVar, Generic

_T_CELL = TypeVar("_T_CELL")

class Cell(Generic[_T_CELL]):
	"""
	Define a cell from a chained list.
	"""
	_value: _T_CELL
	_following: Optional['Cell[_T_CELL]']

	def __init__(self, value: _T_CELL, following: Optional['Cell[_T_CELL]'] = None) -> None:
		self._value = value
		self._following = following

	def __str__(self) -> str:
		display: list[str] = []
		current: Optional[Cell[_T_CELL]] = self.clone()
		while current is not None:
			display.append(str(current.value))
			current = current.following

		return f"<{', '.join(display)}>"

	def __repr__(self) -> str:
		return f"chain.Cell(value={self.value}, following={repr(self.following)})"

	def clone(self) -> 'Cell[_T_CELL]':
		return Cell(
			value=self.value,
			following=self.following,
		)

	@property
	def value(self) -> _T_CELL:
		"""
		Get the read-only `value` of the cell.
		"""
		return self._value

	@property
	def following(self) -> Optional['Cell[_T_CELL]']:
		"""
		Get the read-only `following` next cell. Return `None` if has no following.
		"""
		return self._following

	def set_following(self, new: 'Cell[_T_CELL]') -> None:
		"""
		Set the `following` to a `new` cell.
		"""
		print(f"(?) set_following={new}")
		self._following = new


	def to_list(self) -> list[_T_CELL]:
		"""
		Returns a `list[_T_CELL]` of the values.
		"""
		current: Cell[_T_CELL] = self.clone()
		l: list[_T_CELL] = [current.value]

		while current.following is not None:
			current = current.following
			l.append(current.value)
		
		return l
	
	def go(self, steps: int) -> 'Cell[_T_CELL]':
		"""
		Move up `steps` times, and return the `Cell`.
		Throws an `IndexError` if the index is out of range.
		"""
		current: Cell[_T_CELL] = self.clone()
		
		while steps > 0:
			if current.following is None:
				raise IndexError(f"(X) - modules.chain.Cell.go - Index out of range. steps={steps}, cell={repr(current)}")
			current = current.following

			steps -= 1

		return current

def new_from(values: list[_T_CELL]) -> 'Cell[_T_CELL]':
	"""
	Generate a chained list from a given `values` list.
	"""
	values.reverse()
	current: Cell[_T_CELL] = Cell(values[0])
	for value in values[1:]:
		current = Cell(value, current)

	return current
