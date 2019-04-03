from ledgerlink.models import Saving
from xf.xf_crud.model_lists import XFModelList
from xf.xf_crud.xf_classes import XFUIAction, ACTION_ROW_INSTANCE


class Savinglist(XFModelList):

    def __init__(self, model):
        super(Savinglist, self).__init__(model)
        self.list_field_list = (
            "SavingIdEx", "Member", "Amount", "Meeting"
        )
        self.list_title = "VSLA Saving List"
        self.search_hint = "Code, Name"
        self.list_hint = "Below are the member's savings"
        self.supported_crud_operations.append("search")
        self.preset_filters = {'': 'All'}
        self.add_javascript("ledgerlink_vsla.js")


    def initialise_action_lists(self):
        self.row_action_list.extend(
            (XFUIAction('details', 'View details', 'view', action_type=ACTION_ROW_INSTANCE, use_ajax=False),)
        )

    def get_queryset(self, search_string, model, preset_filter, view_kwargs=None):
        if view_kwargs is not None:
            if "related_fk" in view_kwargs:
                return Saving.objects.filter(Meeting_id = view_kwargs['related_fk'])
        return Saving.objects.all()