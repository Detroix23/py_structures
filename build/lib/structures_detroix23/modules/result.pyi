from typing import TypeVar, Generic

_T_RESULT_OK = TypeVar("_T_RESULT_OK")
_T_RESULT_ERROR = TypeVar("_T_RESULT_ERROR")

class UnwrapException(Exception):
    message: str
    def __init__(self, message: str) -> None: ...

class Result(Generic[_T_RESULT_OK, _T_RESULT_ERROR]):
    ok: _T_RESULT_OK | None
    error: _T_RESULT_ERROR | None
    def __init__(self, ok: _T_RESULT_OK | None, error: _T_RESULT_ERROR | None) -> None: ...
    def unwrap(self) -> _T_RESULT_OK: ...
    def is_ok(self) -> bool: ...
