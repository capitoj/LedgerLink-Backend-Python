from ledgerlink.models import Fine
from xf.xf_crud.model_lists import XFModelList
from xf.xf_crud.xf_classes import XFUIAction, ACTION_ROW_INSTANCE


class FineList(XFModelList):

    def __init__(self, model):
        super(FineList, self).__init__(model)
        self.list_field_list = (
            "FineIdEx",
            "Member",
            "Amount",
            "ExpectedDate",
            "IssuedInMeeting",
            "PaidInMeeting",
            "DateCleared"
        )
        self.list_title = "VSLA Fine List"
        self.search_hint = "Code, Name"
        self.list_hint = "Below are the list of meeting fines"
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
                return Fine.objects.filter(IssuedInMeeting_id = view_kwargs['related_fk'])
        return Fine.objects.all()