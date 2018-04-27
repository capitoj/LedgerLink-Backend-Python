import datetime

from library.models import Book
from xf.xf_system.testing.xf_test_case import XFTestCase


class ValidateBook(XFTestCase):

    def test_title(self):
        self.assertFieldNotClean(Book, "title", "23 years")
        self.assertFieldClean(Book, "title", "25 years")

    def test_publication_date(self):
        self.assertFieldNotClean(Book, 'publication_date', datetime.date.today() + datetime.timedelta(days=21))
        self.assertFieldClean(Book, 'publication_date', datetime.date(1920, 1, 1))
        self.assertFieldNotClean(Book, 'publication_date', datetime.date(1800, 1, 1))

        # Borders
        self.assertFieldClean(Book, 'publication_date', datetime.date.today())
        self.assertFieldClean(Book, 'publication_date', datetime.date.today() - datetime.timedelta(days=1))
        self.assertFieldNotClean(Book, 'publication_date', datetime.date.today() + datetime.timedelta(days=1))


