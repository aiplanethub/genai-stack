"""Util functions for enums."""

from enum import Enum
from typing import List


class StrEnum(str, Enum):
    """Base enum type for string enum values."""

    def __str__(self) -> str:
        """Returns the enum string value.

        Returns:
            The enum string value.
        """
        return self.value  # type: ignore

    @classmethod
    def names(cls) -> List[str]:
        """Get all enum names as a list of strings.

        Returns:
            A list of all enum names.
        """
        return [c.name for c in cls]

    @classmethod
    def values(cls) -> List[str]:
        """Get all enum values as a list of strings.

        Returns:
            A list of all enum values.
        """
        return [c.value for c in cls]