from django.db.models import Q

from ledgerlink.models import Attendance
from xf.xf_crud.model_lists import XFModelList
from xf.xf_crud.xf_classes import XFUIAction, ACTION_ROW_INSTANCE


class AttendanceList(XFModelList):

    def __init__(self, model):
        super(AttendanceList, self).__init__(model)
        self.list_field_list = (
        "AttendanceIdEx", "Member", "Comments", "IsPresent", "Meeting"
        )
        self.list_title = "VSLA Attendance List"
        self.search_hint = "Code, Name"
        self.list_hint = "Below are the list of VSLA meetings"
        # self.supported_crud_operations.append("search")
        self.preset_filters = {'': 'All'}
        self.add_javascript("ledgerlink_vsla.js")


    def initialise_action_lists(self):
        self.instance_action_list.extend(
            (XFUIAction('details', 'View details', 'view', action_type=ACTION_ROW_INSTANCE, use_ajax=False),)
        )

    def get_queryset(self, search_string, model, preset_filter, view_kwargs=None):
        if view_kwargs != None:
            if "related_fk" in view_kwargs:
                return Attendance.objects.filter(Meeting_id = view_kwargs['related_fk'])
        return Attendance.objects.all()