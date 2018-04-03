from django.test import TestCase, SimpleTestCase
import unittest

from library.forms import BookForm, BookList
from library.models import Book
from library.views import BookMasterChildView
from xf.xf_crud.crud_url_builder import XFCrudURLBuilder
from xf.xf_crud.xf_crud_helpers import crudurl


class TestCrudURLBuilder(SimpleTestCase):

    def __init__(self, *args, **kwargs):
        super(TestCrudURLBuilder, self).__init__(*args, **kwargs)
        self.crud_url_builder = None

    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        self.crud_url_builder = XFCrudURLBuilder(url_app_name="library", url_model_name="book", model_type=Book)
        pass

    def test_overview_URL(self):

        url = self.crud_url_builder.get_overview_url(view_class_type=BookMasterChildView)
        self.assertEqual('library_book_overview', url.name)
        self.assertEqual('^library/book/(?P<pk>[-\w]+)/overview', url.regex.pattern)

    def test_details_URL(self):

        url = self.crud_url_builder.get_details_url(form_class_type=BookForm)
        self.assertEqual('library_book_details', url.name)
        self.assertEqual('^library/book/(?P<pk>[-\w]+)/details', url.regex.pattern)

    def test_edit_URL(self):

        url = self.crud_url_builder.get_edit_url(form_class_type=BookForm)
        self.assertEqual('library_book_edit', url.name)
        self.assertEqual('^library/book/(?P<pk>[-\w]+)/edit', url.regex.pattern)


    def test_new_URL(self):

        url = self.crud_url_builder.get_new_url(form_class_type=BookForm)
        self.assertEqual('library_book_new', url.name)
        self.assertEqual('^library/book/new', url.regex.pattern)

    def test_list_URL(self):

        url = self.crud_url_builder.get_list_url(list_class_type=BookList)
        self.assertEqual('library_book_list', url.name)
        self.assertEqual('^library/book/', url.regex.pattern)


    def test_list_preset_filter_URL(self):

        url = self.crud_url_builder.get_list_preset_filter_url(list_class_type=BookList)
        self.assertEqual('library_book_list_filter', url.name)
        self.assertEqual('^library/book/(?P<preset_filter>[-\w]+)', url.regex.pattern)

    def test_list_related_URL(self):

        url = self.crud_url_builder.get_list_related_url(list_class_type=BookList, url_related_name="by-author")
        self.assertEqual('library_book_list_by-author', url.name)
        self.assertEqual('^library/book/by-author/(?P<related_fk>[-\w]+)', url.regex.pattern)
