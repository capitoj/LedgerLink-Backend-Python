from xf.xf_crud.model_lists import XFModelList

class VslaRegionList(XFModelList):

    def __init__(self, model):
        super(VslaRegionList, self).__init__(model)
        self.list_field_list = ('RegionName', 'RegionCode')
        self.list_title = 'VSLA Regions'
        self.search_hint = "Search by name"
        self.supported_crud_operations.append('search')
        self.list_hint = "List of VSLA Regions"