from django.contrib.auth.models import User, Permission, Group
from django.test import TestCase, SimpleTestCase
from django.urls import reverse

from library.forms import BookForm, BookList, ReadOnlyBookList
from library.models import Book
from xf.xf_crud.xf_crud_helpers import crudurl


class TestCRUDOperations(TestCase):

    def __init__(self, *args, **kwargs):
        super(TestCRUDOperations, self).__init__(*args, **kwargs)
        self.urlpatterns = []

    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        self.urlpatterns = crudurl("library/view", "book", Book, BookForm, ReadOnlyBookList)
        pass

    def test_only_list_urls_exist(self):
        self.assertEqual(3, len(self.urlpatterns))
        self.assertEqual("library/view_book_details", self.urlpatterns[0].name)
        self.assertEqual("library/view_book_list_filter", self.urlpatterns[1].name)
        self.assertEqual("library/view_book_list", self.urlpatterns[2].name)