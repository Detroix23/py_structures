"""
# Data structures.
/src/structures_detroix23/modules/base.py.
Base.
"""

from typing import Any
from structures_detroix23.modules import nodes

def verbose_assert_eq(a: Any, b: Any) -> bool:
	"""
	Compare 2 values.
	- raise `AssertionError` if not equal, and prints the values.
	- returns `True` if passed. 
	"""
	if a != b:
		raise AssertionError(f"(X) verbose_assert_eq(a={a}, b={b}) `a` != `b`.")
	else:
		return True
	
def pretty(
	iterable: dict[Any, Any], 
	tab: str = "\t",
	level: int = 0,
) -> str:
	"""
	Return a pretty formatted line broken string of a `dict`.
	"""
	
	lines: list[str] = [tab * level + "{"]

	for key, value in iterable.items():
		result: str

		if isinstance(value, dict):
			result = pretty(value, tab, level + 1)  # pyright: ignore[reportUnknownArgumentType]
		elif isinstance(value, nodes.Node):
			result = value.display(tab)
		else:
			result = value
		lines.append(f"{tab * (level + 1)}{key}: {result}")
		
	lines.append(tab * level + "}")

	return "\n".join(lines)
