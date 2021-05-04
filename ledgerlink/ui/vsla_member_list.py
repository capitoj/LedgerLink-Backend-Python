from ledgerlink.models import Member
from xf.xf_crud.model_lists import XFModelList
from xf.xf_crud.xf_classes import XFUIAction, ACTION_ROW_INSTANCE


class VslaMemberList(XFModelList):

    def __init__(self, model):
        super(VslaMemberList, self).__init__(model)
        self.list_field_list = ("Surname", "OtherNames", "Gender", "Occupation")
        self.list_title = "VSLA Members"
        self.list_hint = "Below is the list of VSLA Members"
        # self.supported_crud_operations = ['list', 'view']
        self.search_hint = "Search by Surname, OtherNames or Gender"
        self.preset_filters = {'': 'All'}
        self.add_javascript("ledgerlink.js")

        # self.row_action_list.append(XFUIAction('details', 'View Members', 'view', use_ajax=False, column_index=1))

    def initialise_action_lists(self):
        self.instance_action_list.extend(
            (XFUIAction('details', 'View details', 'view', action_type=ACTION_ROW_INSTANCE, use_ajax=False, column_index=1),)
        )

    def get_queryset(self, search_string, model, preset_filter, view_kwargs=None):
        if view_kwargs is not None:
            if "related_fk" in view_kwargs:
                return Member.objects.filter(Vsla_id = view_kwargs["related_fk"])
        return Member.objects.all()




