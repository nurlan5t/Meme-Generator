"""Represents a model with a definite message and its author."""


class QuoteModel():
    """A QuoteModel object."""

    def __init__(self, body: str, author: str):
        """Create a QuoteModel object.

        :param body is: Message or a Quote
        :param author is: Author of the Message/Quote
        """
        self.body = body
        self.author = author

    def __repr__(self):
        """Return `repr(self)`, a computer-readable \
           string representation of this object."""
        return f'{self.body}\n-{self.author}'
