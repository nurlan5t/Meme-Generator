"""Create a library that loads data from CSV files.

A 'CSVIngestor' class will parse the CSV file and extract
message body and author, using them to return a collection of
concrete class objects.
"""

from .IngestorInterface import IngestorInterface
from typing import List
import csv
from .QuoteModel import QuoteModel
import pandas


class CSVIngestor(IngestorInterface):
    """Loads and parses data from CSV files.

    :param allowed_extensions - Look for file extension 'csv'.
    """

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the data from CSV file and return \
        a collection of 'Quotes' class objects.

        :param path: Directory of the input file
        """
        if not cls.can_ingest(path):
            raise Exception("cannot ingest exception")

        quotes = []
        data = pandas.read_csv(path, header=0)

        for index, row in data.iterrows():
            meme_msg = QuoteModel(row['body'], row['author'])
            quotes.append(meme_msg)

        return quotes
