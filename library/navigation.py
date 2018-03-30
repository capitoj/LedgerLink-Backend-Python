from django.core.signals import request_started
from django.dispatch import receiver

#from library.models import Book
#from xf.xf_crud.auth.permission_mixin import PermissionMixin
from xf.xf_system.views import XFNavigationViewMixin
from xf.xf_system.xf_navigation import add_navigation


def load_navigation(sender, navigation_trees, request):

    # Each app can create one navigation tree. Navigation trees from multiple apps cannot be merged, by design
    # In this example, the app name is "library"
    #if not navigation_trees.has_key("library"):
    # PYTHON3 UPDATE
    if not "library" in navigation_trees:
        navigation_tree = []
        navigation_trees["library"] = navigation_tree

    #PermissionMixin.user_has_model_perm(Book, "view")

    navigation_tree = navigation_trees["library"]

    add_navigation(navigation_tree, 'Library', "Books", "/library/book/", "fa-world", "Books")
    add_navigation(navigation_tree, 'Library', "Books", "/library/smallbook/", "fa-world", "Small books")
    add_navigation(navigation_tree, 'Library', "Books", "/library/smallbook/", "fa-world", "All", "Small books")
    add_navigation(navigation_tree, 'Library', "Books", "/library/smallbook/recent", "fa-world", "With ZE only",
                   "Small books")
    add_navigation(navigation_tree, 'Library', "Books", "/library/book-instances/", "fa-world", "Instances")
    add_navigation(navigation_tree, 'Library', "Maintenance", "/library/category/", "fa-world", "Categories")

    add_navigation(navigation_tree, 'Library', "Authors", "/library/author/", "fa-world", "Authors")

    add_navigation(navigation_tree, 'Library', "Clients", "/library/client/", "fa-world", "Clients")
    add_navigation(navigation_tree, 'Library', "Clients", "/library/checkout/", "fa-world", "Book checkouts")

    add_navigation(navigation_tree, 'Library', "Maintenance", "/library/library/", "fa-world", "Libraries")


    return



XFNavigationViewMixin.navigation_tree_observers.append(load_navigation)