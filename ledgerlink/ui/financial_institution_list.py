from xf.xf_crud.model_lists import XFModelList

class FinancialInstitutionList(XFModelList):

    def __init__(self, model):
        super(FinancialInstitutionList, self).__init__(model)
        self.list_field_list = (
            "Name",
            "Code"
        )
        self.list_title = "Partner Financial Institutions"
        self.search_hint = "Search by name"
        self.supported_crud_operations.append('search')
        self.list_hint = "Below are a list of financial institutions"
