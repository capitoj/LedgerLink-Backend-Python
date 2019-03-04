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
    # if not "library" in navigation_trees:
    #     navigation_tree = []
    #     navigation_trees["library"] = navigation_tree

    #PermissionMixin.user_has_model_perm(Book, "view")

    if "ledgerlink" not in navigation_trees:
        navigation_tree = []
        navigation_trees["ledgerlink"] = navigation_tree

    navigation_tree = navigation_trees["ledgerlink"]

    add_navigation(navigation_tree, 'Ledgerlink', "Savings Groups", "/crud/savings-groups/post-bank-uganda", "fa-world", "Post Bank")
    add_navigation(navigation_tree, 'Ledgerlink', "Savings Groups", "/crud/savings-groups/finca-uganda/", "fa-world", "Finca Uganda")
    add_navigation(navigation_tree, 'Ledgerlink', "Savings Groups", "/crud/savings-groups/centenary-rural-development-bank/", "fa-world", "Centenary Rural Development Bank")
    add_navigation(navigation_tree, 'Ledgerlink', "Settings", "/crud/financial-institutions/", "fa-world", "Financial Institutions")
    add_navigation(navigation_tree, 'Ledgerlink', "Settings", "/crud/vsla-regions/", "fa-world",
                   "Vsla Regions")
    add_navigation(navigation_tree, 'Ledgerlink', "Settings", "/crud/community-based-trainers/", "fa-world",
                   "Community Based Trainers")
    #
    # add_navigation(navigation_tree, 'Ledgerlink', "Authors", "/library/author/", "fa-world", "Authors")
    #
    # add_navigation(navigation_tree, 'Ledgerlink', "Clients", "/library/client/", "fa-world", "Clients")
    # add_navigation(navigation_tree, 'Ledgerlink', "Clients", "/library/checkout/", "fa-world", "Book checkouts")
    #
    # add_navigation(navigation_tree, 'Ledgerlink', "Maintenance", "/library/library/", "fa-world", "Libraries")


    return



XFNavigationViewMixin.navigation_tree_observers.append(load_navigation)