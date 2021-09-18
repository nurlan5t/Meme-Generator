"""Create a library that loads data from PDF files.

A 'PDFIngestor' class will parse the PDF file and extract
message body and author, using them to return a collection of
concrete class objects.
"""

from typing import List
import subprocess
import os
from random import randint
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Loads and parses data from PDF files.

    :param allowed_extensions - Look for file extension 'pdf'.
    """

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the data from PDF file and return \
        a collection of 'Quotes' class objects.

        :param path: Directory of the input file
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        tmp = f'./tmp/{randint(0,100000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])

        file_ref = open(tmp, "r", encoding='utf-8-sig')
        quotes = []

        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parse = line.split(' - ')
                meme_msg = QuoteModel(str(parse[0]), str(parse[1]))
                quotes.append(meme_msg)

        file_ref.close()
        os.remove(tmp)
        return quotes
