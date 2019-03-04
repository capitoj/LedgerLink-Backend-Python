from ledgerlink.models import FinancialInstitution
from xf.xf_crud.model_forms import XFModelForm


class FinancialInstitutionForm(XFModelForm):

    def __init__(self, *args, **kwargs):
        super(FinancialInstitutionForm, self).__init__(*args, **kwargs)
        self.fields["FinancialInstitutionIdEx"].label = "Financial Institution External ID"


    class Meta:
        model = FinancialInstitution
        title = "Financial Institution"
        fields = ["id", "Name", "Code", "FinancialInstitutionIdEx"]