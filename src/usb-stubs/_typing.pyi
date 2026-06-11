from array import array
from collections.abc import Iterable
from typing import TypeAlias

ReadOnlyDataOrLength: TypeAlias = int | str | bytes | bytearray | Iterable[int] | None
DataOrLength: TypeAlias = ReadOnlyDataOrLength | array[int]
#SizeOrBuffer: TypeAlias = int | array[int]
