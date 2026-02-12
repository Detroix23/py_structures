"""
# Data structures.
/src/structures_detroix23/modules/dynamic_list.py
"""

from typing import Optional, TypeVar, Generic

from structures_detroix23.modules import (
	cell,
)

_T_LIST = TypeVar("_T_LIST")

class DynamicList(Generic[_T_LIST]):
	"""
	# `DynamicList`.
	"""
	data: Optional[cell.Cell[_T_LIST]]

	def __init__(self, data: Optional[cell.Cell[_T_LIST]] = None) -> None:
		self.data = data

	def __len__(self) -> int:
		counter: int = 0

		if self.data is not None:
			current: cell.Cell[_T_LIST] = self.data
			counter += 1

			while current.following is not None:
				current = current.following
				counter += 1

		return counter

	def __repr__(self) -> str:
		if self.is_empty():
			return f"DynamicList(None)"
		else:
			return f"DynamicList({repr(self.data)})"

	def __str__(self) -> str:
		if self.is_empty():
			return f"List<>"
		else:
			return f"List{self.data}"

	def is_empty(self) -> bool:
		"""
		Return `True` if the list is empty.
		"""
		return self.data is None

	def to_list(self) -> list[_T_LIST]:
		if self.data is None:
			return []

		current: cell.Cell[_T_LIST] = self.data
		l: list[_T_LIST] = [current.value]

		while current.following is not None:
			current = current.following
			l.append(current.value)

		return l
	
	def get_last(self) -> cell.Cell[_T_LIST]:
		"""
		Get a reference to the last `Cell` of the list.

		Raises a `ValueError` if the list is empty.
		"""
		if self.data is None:
			raise ValueError(f"(X) modules.dynamic_list.DynamicList.get_last() list ({self}) is empty.")
		
		current: cell.Cell[_T_LIST] = self.data

		while current.following is not None:
			current = current.following
		
		return current


	def push(self, new: cell.Cell[_T_LIST]) -> None:
		"""
		Add a `Cell` to the `following` of the last current `Cell`. 
		"""
		if self.data is None:
			self.data = new

		else:
			last = self.get_last()
			print(f"(?) last={last}", end=" ")
			last.set_following(new)
			print(f"(?) last={last}, self.get_last={self.get_last()}")


	def append(self, value: _T_LIST) -> None:
		"""
		Add an item `value` to the end of the list.

		Creates a new `Cell` englobing the `value. 
		"""
		self.push(cell.Cell(value, None))
	
