from django.test import TestCase, SimpleTestCase

from library.models import Book
from library.tests.xf_crud_tests.mixins import CreateUsersMixin
from xf_crud.model_lists import XFModelList
from xf_crud.xf_classes import XFUIAction


class TestActions(TestCase, CreateUsersMixin):

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.setup_user_and_permission_data()

    def setUp(self):
        super().setUp()
        self.book_list = XFModelList(Book)


    def test_default_action_list_created(self):

        # ['add', 'change', 'delete', 'view', 'list']
        self.assertEqual(1, len(self.book_list.screen_actions))
        self.assertEqual(3, len(self.book_list.row_action_list))

    def test_adding_overview_view(self):
        self.book_list.row_default_action = XFUIAction('overview', 'Lots of details', 'view', use_ajax=False)
        self.assertIsInstance(self.book_list.row_default_action, XFUIAction)
        self.assertEqual(self.book_list.row_default_action.url_name, "%s_%s_overview")

    def test_add_action_created(self):
        self.assertIsInstance(self.book_list.get_action('new'), XFUIAction)
        self.assertEqual(self.book_list.get_action('new').url_name, "%s_%s_new")

    def test_edit_action_created(self):
        self.assertIsInstance(self.book_list.get_entity_action('edit'), XFUIAction)
        self.assertEqual(self.book_list.get_entity_action('edit').url_name, "%s_%s_edit")

    def test_delete_action_created(self):
        self.assertIsInstance(self.book_list.get_entity_action('delete'), XFUIAction)
        self.assertEqual(self.book_list.get_entity_action('delete').url_name, "%s_%s_delete")

    def test_details_action_created(self):
        self.assertIsInstance(self.book_list.get_entity_action('details'), XFUIAction)
        self.assertEqual(self.book_list.get_entity_action('details').url_name, "%s_%s_details")
