from xf.xf_crud.model_lists import XFModelList
from xf.xf_crud.xf_classes import XFUIAction


class VslaList(XFModelList):

    def __init__(self, model):
        super(VslaList, self).__init__(model)
        self.list_field_list = ("VslaCode", "VslaName", "VslaPhoneMsisdn", "PhoneNumber", "NumberOfCycles")
        self.list_title = "VSLA List"
        self.search_hint = "Code, Name"
        self.list_hint = "Below are the list of VSLAs"
        self.supported_crud_operations.append("search")
        self.preset_filters = {'':'All'}
        self.add_javascript("ledgerlink_vsla.js")

        self.row_action_list.append(XFUIAction('overview', 'View Cycles', 'view', use_ajax=False, column_index=1))

        def prepare_actions(self):
            super().prepare_actions()
            # self.instance_action_list.remove(self.get_entity_action('delete'))
