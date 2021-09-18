"""Create a library that loads data from TXT files.

A 'CSVIngestor' class will parse the TXT file and extract
message body and author, using them to return a collection of
concrete class objects.
"""

from typing import List
import os

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TXTIngestor(IngestorInterface):
    """Loads and parses data from TXT files.

    :param allowed_extensions - Look for file extension 'txt'.
    """

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the data from TXT file and return \
        a collection of 'Quotes' class objects.

        :param path: Directory of the input file
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        file_ref = open(path, "r", encoding='utf-8-sig')
        quotes = []

        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parse = line.split(' - ')
                meme_msg = QuoteModel(str(parse[0]), str(parse[1]))
                quotes.append(meme_msg)

        file_ref.close()
        return quotes
