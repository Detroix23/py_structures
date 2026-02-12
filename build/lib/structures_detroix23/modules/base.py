"""
# Data structures.
/src/structures_detroix23/modules/base.py.
Base.
"""

def verbose_assert_eq(a: object, b: object) -> bool:
	"""
	Compare 2 values.
	- raise `AssertionError` if not equal, and prints the values.
	- returns `True` if passed. 
	"""
	if a != b:
		raise AssertionError(f"(X) verbose_assert_eq(a={a}, b={b}) `a` != `b`.")
	else:
		return True
