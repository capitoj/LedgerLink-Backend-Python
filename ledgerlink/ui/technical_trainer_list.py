from xf.xf_crud.model_lists import XFModelList

class TechnicalTrainerList(XFModelList):

    def __init__(self, model):
        super(TechnicalTrainerList, self).__init__(model)
        self.list_field_list = (
            "Username",
            "FirstName",
            "LastName",
            "Email",
            "PhoneNumber",
            "Status"
        )
        self.list_title = "Community Based Trainers"
        self.search_hint = "Search by FirstName, LastName, Email, PhoneNumber"
        self.supported_crud_operations.append('search')
        self.list_hint = "Below are a list of Community Based Trainers"