from django.contrib.auth.models import User, Permission, Group


class CreateUsersMixin():

    @staticmethod
    def setup_user_and_permission_data():
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



