from django.contrib.auth.models import User, Permission, Group
from django.test import SimpleTestCase
from django.urls import reverse

from library.forms import BookForm, BookList
from library.models import Book
from library.tests.xf_crud_tests.mixins import CreateUsersMixin
from xf_crud.generic_crud_views import XFCreateView
from xf_crud.model_lists import XFModelList
from xf_crud.xf_classes import XFActionType, XFModelListAction, XFUIBuilder
from xf_crud.xf_crud_helpers import crudurl


class TestUIBuilder(SimpleTestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):

        self.uiBuilder = XFUIBuilder(url_app_name="library",
                                model_type=Book,
                                list_class_type=BookList,
                                form_class_type=BookForm)
        pass



    def test_ui_builder_action_new(self):

        new_action = self.uiBuilder.generate_action(XFActionType.SINGLE_ENTITY_NEW, 'new', 'Create new')
        self.assertEqual('library_book_new', new_action.url_name)

    def test_ui_builder_url_new(self):

        url = self.uiBuilder.generate_url('add')
        self.assertEqual('library_book_new', url.name)
        self.assertEqual('/library/book/new', reverse(url.name))

