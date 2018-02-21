from django.test import TestCase, SimpleTestCase
import unittest

from library.forms import BookForm, BookList
from library.models import Book
from xf_crud.xf_crud_helpers import crudurl


class TestCrudURLs(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestCrudURLs, self).__init__(*args, **kwargs)
        self.urlpatterns = []

    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        self.urlpatterns = crudurl("library", "book", Book, BookForm, BookList)
        pass


    def test_crud_new_urls(self):
        self.assertEqual('library_book_new', self.urlpatterns[0].name)
        self.assertEqual('^library/book/new', self.urlpatterns[0].regex.pattern)
        pass

    def test_crud_edit_urls(self):
        self.assertEqual('library_book_edit', self.urlpatterns[1].name)
        self.assertEqual('^library/book/(?P<pk>[-\w]+)/edit', self.urlpatterns[1].regex.pattern)

    def test_crud_details_urls(self):
        self.assertEqual('library_book_details', self.urlpatterns[2].name)
        self.assertEqual('^library/book/(?P<pk>[-\w]+)/details', self.urlpatterns[2].regex.pattern)

    def test_crud_delete_urls(self):
        self.assertEqual('library_book_delete', self.urlpatterns[3].name)
        self.assertEqual('^library/book/(?P<pk>[-\w]+)/delete', self.urlpatterns[3].regex.pattern)

    def test_crud_list_filter_urls(self):
        self.assertEqual('library_book_list_filter', self.urlpatterns[4].name)
        self.assertEqual('^library/book/(?P<preset_filter>[-\w]+)', self.urlpatterns[4].regex.pattern)

    def test_crud_list_urls(self):
        self.assertEqual('library_book_list', self.urlpatterns[5].name)
        self.assertEqual('^library/book/', self.urlpatterns[5].regex.pattern)
