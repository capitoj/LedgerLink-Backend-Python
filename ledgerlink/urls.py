from ledgerlink.models import VslaRegion, Vsla, FinancialInstitution, TechnicalTrainer, VslaCycle, Meeting
from ledgerlink.ui.attendance_list import AttendanceList
from ledgerlink.ui.financial_institution_form import FinancialInstitutionForm
from ledgerlink.ui.financial_institution_list import FinancialInstitutionList
from ledgerlink.ui.meeting_list import MeetingList
from ledgerlink.ui.technical_trainer_form import TechnicalTrainerForm
from ledgerlink.ui.technical_trainer_list import TechnicalTrainerList
from ledgerlink.ui.vsla_cycle_list import VslaCycleList
from ledgerlink.ui.vsla_form import VslaForm
from ledgerlink.ui.vsla_list import VslaList
from ledgerlink.ui.vsla_region_form import VslaRegionForm
from ledgerlink.ui.vsla_region_list import VslaRegionList
from ledgerlink.views import VslaMasterChildView, VslaInstanceMasterChildView, VslaCycleInstanceMasterChildView, \
    MeetingAttendanceMasterChildView
from xf.xf_crud.crud_url_builder import XFCrudURLBuilder
from xf.xf_crud.xf_crud_helpers import crudurl

urlpatterns = []

#URL Builders

vsla_builder = XFCrudURLBuilder(url_app_name="crud", url_model_name="savings-groups", model_type=Vsla)
vsla_instance_builder = XFCrudURLBuilder(url_app_name="crud", url_model_name="savings-group-cycle", model_type=VslaCycle)
vsla_cycle_instance_builder = XFCrudURLBuilder(url_app_name="crud", url_model_name="savings-group-meeting", model_type=Meeting)
# meeting_attendance_instance_builder = XFCrudURLBuilder(url_app_name="crud", url_model_name="savings-group-meeting-attendance", model_type=Meeting)
#
# #List of Cycles by VSLA
urlpatterns += [vsla_builder.get_list_related_url(list_class_type=VslaList, url_related_name="by-institution", foreign_key_name="financialinstitution")]
urlpatterns += [vsla_instance_builder.get_list_related_url(list_class_type=VslaCycleList, url_related_name="by-vsla", foreign_key_name="vsla")]
urlpatterns += [vsla_cycle_instance_builder.get_list_related_url(list_class_type=MeetingList, url_related_name="by-cycle", foreign_key_name="vslacycle")]
# urlpatterns += [meeting_attendance_instance_builder.get_list_related_url(list_class_type=AttendanceList, url_related_name="by-meeting", foreign_key_name="meeting")]
#
# #Master Child pages
#
urlpatterns += [vsla_builder.get_overview_url(view_class_type=VslaMasterChildView)]
urlpatterns += [vsla_instance_builder.get_overview_url(view_class_type=VslaInstanceMasterChildView)]
urlpatterns += [vsla_cycle_instance_builder.get_overview_url(view_class_type=VslaCycleInstanceMasterChildView)]
# urlpatterns += [meeting_attendance_instance_builder.get_overview_url(view_class_type=MeetingAttendanceMasterChildView)]

# urlpatterns += [vsla_cycle_instance_builder.get_overview_url(view_class_type=MeetingInstanceMasterChildView)]

## Basic CRUD pages

urlpatterns += crudurl("crud", "savings-group-cycle", VslaCycle, None, VslaCycleList)
urlpatterns += crudurl("crud", "savings-group-meeting", Meeting, None, MeetingList)
urlpatterns += crudurl("crud", "savings-groups", Vsla, VslaForm, VslaList)
urlpatterns += crudurl("crud", "financial-institutions", FinancialInstitution, FinancialInstitutionForm, FinancialInstitutionList)
urlpatterns += crudurl("crud", "vsla-regions", VslaRegion, VslaRegionForm, VslaRegionList)
urlpatterns += crudurl("crud", "community-based-trainers", TechnicalTrainer, TechnicalTrainerForm, TechnicalTrainerList)