"""
# Data structures.
/src/structures_detroix23/modules/graphs.py
"""

from typing import Optional

from structures_detroix23.modules import (
	nodes,
)

class Graph:
	"""
	Describe abstractly the base of any `Graph` representation.
	"""
	register: list[nodes.Node]

	def __init__(
		self, 
		register: Optional[list[nodes.Node]]
	) -> None:
		self.register = register if register is not None else []


class Explorer:
	"""
	Allows the exploring of a graph without infinite recursion.
	""" 
	graph: Graph
	current: nodes.Node
	seen: set[nodes.Node]

	def __init__(self, graph: Graph, current: nodes.Node) -> None:
		self.graph = graph
		self.current = current
		self.seen = set()
		

	def move(self, destination: nodes.Node) -> bool:
		"""
		Move to a `Node`. Return `True` if succeed, `False` if:
		- is not reachable from `current`,
		- has already been `seen`.
		"""
		if (
			destination in self.current.get_next().keys()
			and destination not in self.seen
		):
			self.current = destination
			return True
		
		return False
	


	
