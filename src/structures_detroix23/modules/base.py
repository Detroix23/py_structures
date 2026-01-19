"""
# Data structures.
/src/structures_detroix23/modules/base.py.
Base.
"""

from typing import Any

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
	