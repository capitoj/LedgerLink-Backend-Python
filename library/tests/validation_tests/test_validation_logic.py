import datetime

from library.models import Book
from xf.xf_system.testing.extended_test_case import ExtendedTestCase


class ValidateBook(ExtendedTestCase):

    def test_title(self):
        self.assertNotClean(Book, "title", "23 years")
        self.assertClean(Book, "title", "25 years")

    def test_publication_date(self):
        self.assertNotClean(Book, 'publication_date', datetime.date.today() + datetime.timedelta(days=21))
        self.assertClean(Book, 'publication_date', datetime.date(1920, 1, 1))
        self.assertNotClean(Book, 'publication_date', datetime.date(1800, 1, 1))

        # Borders
        self.assertClean(Book, 'publication_date', datetime.date.today())
        self.assertClean(Book, 'publication_date', datetime.date.today() - datetime.timedelta(days=1))
        self.assertNotClean(Book, 'publication_date', datetime.date.today() + datetime.timedelta(days=1))


