"""Represents an abstract base class library \
that parses an input file of a certain well-defined extension."""

from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Create a class with methods to load \
    and parse any file.

    :list allowed_extensions - Collection of file extension
    """

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Return true if the file has a well defined extension \
         which can be loaded and parsed.

        :param path: Directory of the desired file
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract method which can be encapsulated \
        by other user-defined helper classes realized \
        from the ABC."""
        pass
