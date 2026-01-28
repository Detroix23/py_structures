"""
# Data structures.
/src/structures_detroix23/modules/nodes.py.
"""

from typing import Optional, TypeVar, Generic

_T_RESULT_ERROR = TypeVar("_T_RESULT_ERROR")
_T_RESULT_OK = TypeVar("_T_RESULT_OK")


class UnwrapException(Exception):
	"""
	# `UnwrapException`.
	Raised when trying to unwrap a `Result` containing an error.
	"""
	message: str

	def __init__(self, message: str) -> None:
		super().__init__(message)
		self.message = message

	def __str__(self) -> str:
		return super().__str__()


class Result(Generic[_T_RESULT_OK, _T_RESULT_ERROR]):
	"""
	# `Result`.
	Rust like `Result`, containing or an error, or a success value. 

	Define 2 generics:
	1. `_T_RESULT_OK`,
	2. `_T_RESULT_ERROR`.
	"""
	ok: Optional[_T_RESULT_OK]
	error: Optional[_T_RESULT_ERROR]

	def __init__(
		self, 
		ok: Optional[_T_RESULT_OK], 
		error: Optional[_T_RESULT_ERROR]
	) -> None:
		self.ok = ok
		self.error = error
	
	def unwrap(self) -> _T_RESULT_OK:
		"""
		Return the `ok` value. If there is an `error, raise an `UnwrapException`. 
		"""
		if self.error is not None or self.ok is None:
			raise UnwrapException(str(self.error))
		
		return self.ok

	def is_ok(self) -> bool:
		"""
		Return `True` if no error.
		"""
		return self.error is None and self.ok is not None
