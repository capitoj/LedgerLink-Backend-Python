import unittest
import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase

from library.models import Book


class ValidateBook(TestCase):

    def test_title(self):
        book = Book()
        book.title = "23 years"
        with self.assertRaises(ValidationError) as ex:
            book.clean()
        self.assertIn("title", ex.exception.message_dict)

        book.title = "24 years"
        try:
            book.clean()
        except ValidationError:
            self.fail("Clean raised ValidationError unexpectedly")

    def test_publication_date(self):
        book = Book()
        book.publication_date = datetime.date.today() + datetime.timedelta(days=21)
        with self.assertRaises(ValidationError) as ex:
            book.clean()
        self.assertIn("publication_date", ex.exception.message_dict)

        book.publication_date = datetime.date(1800, 1, 1)
        with self.assertRaises(ValidationError) as ex:
            book.clean()
        self.assertIn("publication_date", ex.exception.message_dict)

        book.publication_date = datetime.date(1920, 1, 1)
        try:
            book.clean()
        except ValidationError:
            self.fail("Clean raised ValidationError unexpectedly")
