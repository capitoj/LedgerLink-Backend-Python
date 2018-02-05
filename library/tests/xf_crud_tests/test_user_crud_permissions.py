from django.contrib.auth.models import User, Permission, Group
from django.test import TestCase, SimpleTestCase
from django.urls import reverse

from library.forms import BookForm, BookList
from library.models import Book
from xf_crud.xf_crud_helpers import crudurl


class TestCRUDPermissions(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.set_up_user_data()

    @classmethod
    def set_up_user_data(cls):

        User.objects.create_user(username="admin_user", email="@", password="!2345678", first_name="admin",
                                 is_superuser=True)
        read_only_user = User.objects.create_user(username="read_only_user", email="@", password="!2345678",
                                                  first_name="read_only")
        read_only_group = Group.objects.create(name="read_only_group")
        read_only_group.permissions.add(Permission.objects.get(codename="view_book"))
        read_only_group.permissions.add(Permission.objects.get(codename="list_book"))
        read_only_group.user_set.add(read_only_user)

        full_rights_user = User.objects.create_user(username="full_rights_user", email="@", password="!2345678",
                                                    first_name="full_rights")
        full_rights_group = Group.objects.create(name="full_rights_group")
        full_rights_group.permissions.add(Permission.objects.get(codename="view_book"))
        full_rights_group.permissions.add(Permission.objects.get(codename="list_book"))
        full_rights_group.permissions.add(Permission.objects.get(codename="add_book"))
        full_rights_group.permissions.add(Permission.objects.get(codename="change_book"))
        full_rights_group.permissions.add(Permission.objects.get(codename="delete_book"))
        full_rights_group.user_set.add(full_rights_user)

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
        self.assertTrue(response.context_data['view'])
        self.assertFalse(response.context_data['change'])
        self.assertFalse(response.context_data['add'])
        self.assertFalse(response.context_data['delete'])
        pass

    def test_book_full_rights_list(self):
        self.client.login(username='full_rights_user', password='!2345678')
        response = self.client.get(reverse('library_book_list'))

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context_data['search'])  # corresponds to list permission
        self.assertTrue(response.context_data['view'])
        self.assertTrue(response.context_data['change'])
        self.assertTrue(response.context_data['add'])
        self.assertTrue(response.context_data['delete'])
        pass

