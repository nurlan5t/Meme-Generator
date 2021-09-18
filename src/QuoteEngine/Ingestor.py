"""Represents a library that is realized from ABC \
that provides one simplified method of parsing \
an input file of well-defined extension."""

from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .TXTIngestor import TXTIngestor


class Ingestor(IngestorInterface):
    """Create a strategic class that realizes \
    from ABC that uses different strategic objects \
    to handle different file types."""

    ingestors = [DocxIngestor, CSVIngestor, PDFIngestor, TXTIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the data from a file having valid and well-defined.

        extension, through its respective strategic object.
        Returns a collection of 'QuoteModel' class objects for
        each file type.

        :param path: Directory of the input file
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
