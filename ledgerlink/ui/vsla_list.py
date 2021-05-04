from xf.xf_crud.model_lists import XFModelList
from xf.xf_crud.xf_classes import XFUIAction
from ledgerlink.models.vsla import Vsla
from ledgerlink.models.financial_institution import FinancialInstitution
from django.db.models import Q


class VslaList(XFModelList):

    def __init__(self, model):
        super(VslaList, self).__init__(model)
        self.list_field_list = ("VslaCode", "VslaName", "VslaPhoneMsisdn", "PhoneNumber", "NumberOfCycles")
        self.list_title = "VSLA List"
        self.search_hint = "VSLA Name, Physical Address"
        self.list_hint = "Below are the list of VSLAs"
        self.supported_crud_operations.append("search")
        self.preset_filters = {'':'All'}
        self.add_javascript("ledgerlink.js")

        self.instance_action_list.append(XFUIAction('overview', 'View Cycles', 'view', use_ajax=False, column_index=1))

    def prepare_actions(self):
        super().prepare_actions()
        self.instance_action_list.remove(self.get_entity_action('delete'))

    def get_queryset(self, search_string, model, preset_filter, view_kwargs=None):

        financial_institution_ids = []
        if "preset_filter" in view_kwargs:
            if self.request.user.has_perm(view_kwargs.get("preset_filter")):
                model_objects = FinancialInstitution.objects.filter(Code__in = [view_kwargs.get("preset_filter")])
                if model_objects.count() == 1:
                    for model_object in model_objects:
                        financial_institution_ids.append(model_object.id)
                    return Vsla.objects.filter(FinancialInstitution_id__in = financial_institution_ids).filter(Q(VslaName__icontains=search_string) | Q(PhysicalAddress__icontains=search_string))
                else:
                    return Vsla.objects.none()
            else:
                return Vsla.objects.none()
        else:
            if self.request.user.is_superuser:
                financial_institutions = FinancialInstitution.objects.all()
                for model_object in financial_institutions:
                    if self.request.user.has_perm(model_object.Code):
                        financial_institution_ids.append(model_object.id)

                if len(financial_institution_ids) > 0:
                    return Vsla.objects.filter(FinancialInstitution_id__in = financial_institution_ids).filter(Q(VslaName__icontains=search_string) | Q(PhysicalAddress__icontains=search_string))
                else:
                    return Vsla.objects.none()
            else:
                return Vsla.objects.none()