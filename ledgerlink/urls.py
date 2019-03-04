from ledgerlink.models import VslaRegion, Vsla, FinancialInstitution, TechnicalTrainer
from ledgerlink.ui.financial_institution_form import FinancialInstitutionForm
from ledgerlink.ui.financial_institution_list import FinancialInstitutionList
from ledgerlink.ui.technical_trainer_form import TechnicalTrainerForm
from ledgerlink.ui.technical_trainer_list import TechnicalTrainerList
from ledgerlink.ui.vsla_form import VslaForm
from ledgerlink.ui.vsla_list import VslaList
from ledgerlink.ui.vsla_region_form import VslaRegionForm
from ledgerlink.ui.vsla_region_list import VslaRegionList
from xf.xf_crud.xf_crud_helpers import crudurl

urlpatterns = []


## Basic CRUD pages

urlpatterns += crudurl("crud", "savings-groups", Vsla, VslaForm, VslaList)
urlpatterns += crudurl("crud", "financial-institutions", FinancialInstitution, FinancialInstitutionForm, FinancialInstitutionList)
urlpatterns += crudurl("crud", "vsla-regions", VslaRegion, VslaRegionForm, VslaRegionList)
urlpatterns += crudurl("crud", "community-based-trainers", TechnicalTrainer, TechnicalTrainerForm, TechnicalTrainerList)