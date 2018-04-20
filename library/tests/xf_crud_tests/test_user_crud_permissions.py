from django.contrib.auth.models import User, Permission, Group
from django.test import TestCase, SimpleTestCase
from django.urls import reverse

from library.forms import BookForm, BookList
from library.models import Book
from library.tests.xf_crud_tests.mixins import CreateUsersMixin
from xf.xf_crud.xf_crud_helpers import crudurl


class TestCRUDPermissions(TestCase, CreateUsersMixin):

    @classmethod
    def setUpTestData(cls):
        cls.setup_user_and_permission_data()


    def test_verify_user_created(self):
        admin_user = User.objects.get(username="admin_user")
        read_only = User.objects.get(username="read_only_user")
        self.assertEqual("admin", admin_user.first_name)
        read_only.get_all_permissions()

    def test_read_only_user_permissions(self):
        read_only_user = User.objects.get(username="read_only_user")
        permissions = read_only_user.get_all_permissions()
        self.assertTrue('library.list_book' in permissions)
        self.assertTrue('library.view_book' in permissions)
        self.assertFalse('library.change_book' in permissions)
        self.assertFalse('library.delete_book' in permissions)
        self.assertFalse('library.add_book' in permissions)

    def test_full_rights_user_permissions(self):
        read_only_user = User.objects.get(username="full_rights_user")
        permissions = read_only_user.get_all_permissions()
        self.assertTrue('library.list_book' in permissions)
        self.assertTrue('library.view_book' in permissions)
        self.assertTrue('library.change_book' in permissions)
        self.assertTrue('library.delete_book' in permissions)
        self.assertTrue('library.add_book' in permissions)

    def test_book_read_only_list(self):
        self.client.login(username='read_only_user', password='!2345678')
        response = self.client.get(reverse('library_book_list'))

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context_data['search'])  # corresponds to list permission
        pass

    def test_book_full_rights_list(self):
        self.client.login(username='full_rights_user', password='!2345678')
        response = self.client.get(reverse('library_book_list'))

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context_data['search'])  # corresponds to list permission
        pass

