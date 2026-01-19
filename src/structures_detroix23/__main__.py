"""
# Data structures.
/src/structures_detroix23/__main__.py
Main file.
"""

import sys

from structures_detroix23.modules import (
	base,
	cell,
	dynamic_list,
)

def test_chain1() -> None:
	"""
	Main chained list test entry point.
	"""
	print("\n(?) main.test_chain1() Start.")

	base.verbose_assert_eq(cell.Cell(1).to_list(), [1])

	assert (cell.Cell(1, cell.Cell(2, cell.Cell(3)))).to_list() == [1, 2, 3]
	
	c3: cell.Cell[int] = cell.new_from([1, 2, 3, 4])
	assert c3.to_list() == [1, 2, 3, 4]

	base.verbose_assert_eq(c3.go(0).value, 1)
	base.verbose_assert_eq(c3.go(1).value, 2)
	base.verbose_assert_eq(c3.go(2).value, 3)
	base.verbose_assert_eq(c3.go(3).value, 4)

	print("(?) main.test_chain1() Passed.\n")
	return

def test_list1() -> None:
	print("\n(?) main.test_chain1() Start.")

	c1: cell.Cell[int] = cell.new_from([3, 4, 5])

	l1: dynamic_list.DynamicList[int] = dynamic_list.DynamicList()
	l1.append(1)
	l1.append(2)
	l1.push(c1)

	print(f"l1={l1}, len={len(l1)}, l={l1.to_list()}")

	l2: dynamic_list.DynamicList[int] = dynamic_list.DynamicList()
	print(f"l2={l2}, len={len(l2)}, l={l2.to_list()}")

	l3: dynamic_list.DynamicList[int] = dynamic_list.DynamicList()
	l3.append(1)
	print(f"l3={l3}, len={len(l3)}, l={l3.to_list()}")

	print("(?) main.test_chain1() Passed.\n")
	return

def help() -> str:
	return """## Help.

Get some help.
"""

def test() -> None:
	print("## Tests.")

	test_chain1()
	test_list1()

	return	

def main() -> None:
	print("# Data structures.")

	arguments: list[str] = sys.argv
	selected: int = 0

	for argument in arguments:
		if argument in {"--test", "-t"}:
			selected += 1
			test()
	
	if selected == 0:
		help()

	return

main()
