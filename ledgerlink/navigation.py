from django.core.signals import request_started
from django.dispatch import receiver

from xf.xf_system.views import XFNavigationViewMixin
from xf.xf_system.xf_navigation import add_navigation


def load_navigation(sender, navigation_trees, request):
    from ledgerlink.models.financial_institution import FinancialInstitution

    if request.user.is_authenticated:

        if "ledgerlink" not in navigation_trees:
            navigation_tree = []
            navigation_trees["ledgerlink"] = navigation_tree

        navigation_tree = navigation_trees["ledgerlink"]

        if request.user.has_perm('ledgerlink.rural_finance_initiative'):
            FinancialInstitutions = FinancialInstitution.objects.filter(Code='rural_finance_initiative')
            for object in FinancialInstitutions:
                add_navigation(navigation_tree, 'Ledgerlink', "Savings Groups", "/crud/savings-groups/" + object.Code,
                               "fa-world", object.Name)

        if request.user.is_superuser:
            add_navigation(navigation_tree, 'Ledgerlink', "Settings", "/crud/financial-institutions/", "fa-world", "Financial Institutions")
            add_navigation(navigation_tree, 'Ledgerlink', "Settings", "/crud/vsla-regions/", "fa-world",
                           "Vsla Regions")
            add_navigation(navigation_tree, 'Ledgerlink', "Settings", "/crud/community-based-trainers/", "fa-world",
                           "Community Based Trainers")

    return


XFNavigationViewMixin.navigation_tree_observers.append(load_navigation)