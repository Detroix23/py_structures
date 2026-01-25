"""
# Data structures.
/src/structures_detroix23/modules/nodes.py.
"""

from typing import Optional, Self, Iterable

from structures_detroix23.modules.types import Weight 
from structures_detroix23.modules import (
	base,
)

class Node:
	"""
	# `Node`.
	Define a named cell, holding no value except:  
	- `_name`: `str`, a globally unique name.
	- `_previous`: `dict['Node', Weight]`, containing as many references to other nodes.
	- `_next`: `dict['Node', Weight]`, containing as many references to other nodes.

	Class variables:
	- `last_id`: `int`, store the last created id, to ensure uniqueness.
	"""
	_last_id: int = 0

	_id: int
	_name: str
	_previous: dict['Node', Weight]
	_next: dict['Node', Weight]

	def __new__(
		cls,
		name: str,
		previous: Optional[dict['Node', Weight]] = None,
		next: Optional[dict['Node', Weight]] = None,
	) -> Self:
		new: Self = super(Node, cls).__new__(cls)
		
		new._id = Node._last_id
		Node._last_id += 1

		return new

	def __init__(
		self, 
		name: str,
		previous: Optional[dict['Node', Weight]] = None,
		next: Optional[dict['Node', Weight]] = None,
	) -> None:
		"""
		Instantiate a new `Node`.
		- `name` must be unique globally.
		"""
		self._name = name
		self._previous = previous if previous is not None else {}
		self._next = next if next is not None else {}

	def __hash__(self) -> int:
		return self.get_id()

	def __repr__(self) -> str:
		return f"Node(name={self._name}, id={self._id}, previous={self._previous}, next={self._next})"

	def __str__(self) -> str:
		return f"{self._name}({self.get_id()})"

	def get_id(self) -> int:
		"""
		Returns the unique, read-only `_id` of the `Node`.
		"""
		return self._id

	def get_name(self) -> str:
		"""
		Returns the read-only `_name` of the `Node`.
		"""
		return self._name

	def get_previous(self) -> dict['Node', Weight]:
		"""
		Returns the read-only `_previous` of the `Node`.
		"""
		return self._previous
	
	def get_next(self) -> dict['Node', Weight]:
		"""
		Returns the read-only `_next` of the `Node`.
		"""
		return self._next
	
	def set_previous(self, node: 'Node', weight: Weight) -> None:
		"""
		Create or update in `previous` the `node` with `weight`.
		"""
		self._previous[node] = weight

	def set_next(self, node: 'Node', weight: Weight) -> None:
		"""
		Create or update in `next` the `node` with `weight`.
		"""
		self._next[node] = weight

	def batch_previous(self, nodes: Iterable[tuple['Node', Weight]]) -> None:
		"""
		Update multiple `nodes` in `previous`, from an `Iterable` of `(Node, Weight)`.
		"""
		for node, weight in nodes:
			self.set_previous(node, weight)

	def batch_next(self, nodes: Iterable[tuple['Node', Weight]]) -> None:
		"""
		Update multiple `nodes` in `next`, from an `Iterable` of `(Node, Weight)`.
		"""
		for node, weight in nodes:
			self.set_next(node, weight)


	def remove_previous(self, node: 'Node') -> Optional[Weight]:
		"""
		Remove the given `node` from `previous`.
		
		Return the weight, or `None` if `node` didn't existed. 
		"""
		self._previous.pop(node, None)
	
	def remove_next(self, node: 'Node') -> Optional[Weight]:
		"""
		Remove the given `node` from `next`.
		
		Return the weight, or `None` if `node` didn't existed. 
		"""
		self._next.pop(node, None)

	def display(self, tab: str, level: int = 0) -> str:
		"""
		Multiple line readable representation of the `Node`.
		"""
		lines: list[str] = [f"{self.get_name()}({self.get_id()})\n"]

		lines.append(f"- previous: {base.pretty(self.get_previous(), tab, level)}")
		lines.append(f"- next: {base.pretty(self.get_next(), tab, level)}")

		return "\n".join(lines)
	
