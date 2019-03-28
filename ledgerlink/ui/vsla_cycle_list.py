from xf.xf_crud.model_lists import XFModelList
from xf.xf_crud.xf_classes import XFUIAction


class VslaCycleList(XFModelList):

    def __init__(self, model):
        super(VslaCycleList, self).__init__(model)
        self.list_field_list = (
            "StartDate",
            "EndDate",
            "InterestRate",
            "SharePrice",
            "MigratedInterest",
            "MigratedFines"
        )
        self.list_title = "Vsla Cycles"
        self.search_hint = "Search by StartDate, EndDate, InterestRate"
        self.supported_crud_operations.append('search')
        self.list_hint = "Below is a list of cycles"

        self.row_action_list.append(XFUIAction('overview', 'View Meetings', 'view', use_ajax=False, column_index=1))