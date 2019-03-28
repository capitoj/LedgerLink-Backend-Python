from xf.xf_crud.model_lists import XFModelList
from xf.xf_crud.xf_classes import XFUIAction

class AttendanceList(XFModelList):

    def __init__(self, model):
        super(AttendanceList, self).__init__(model)
        self.list_field_list = (
        "AttendanceIdEx", "Member", "Comments", "IsPresent"
        )
        self.list_title = "VSLA Attendance List"
        self.search_hint = "Code, Name"
        self.list_hint = "Below are the list of VSLA meetings"
        self.supported_crud_operations.append("search")
        self.preset_filters = {'': 'All'}
        self.add_javascript("ledgerlink_vsla.js")