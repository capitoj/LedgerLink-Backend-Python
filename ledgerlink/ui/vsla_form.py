from ledgerlink.models import Vsla
from xf.xf_crud.model_forms import XFModelForm

class VslaForm(XFModelForm):

    def __init__(self, *args, **kwargs):
        super(VslaForm, self).__init__(*args, **kwargs)
        self.fields["VslaCode"].label = "Vsla Code"
        self.fields["VslaName"].label = "Vsla Name"
        self.fields["VslaPhoneMsisdn"].label = "Phone MSISDN"
        self.fields["PhysicalAddress"].label = "Physical Address"
        self.fields["GpsLocation"].label = "GPS Location"
        self.fields["DateRegistered"].label = "Date Registered"
        self.fields["DateLinked"].label = "Date Linked"
        self.fields["Region"].label = "Region"
        self.fields["ContactPerson"].label = "Contact Person"
        self.fields["PositionInVsla"].label = "Position In Vsla"
        self.fields["PhoneNumber"].label = "Phone Number"
        self.fields["GroupAccountNumber"].label = "Account Number"
        self.fields["NumberOfCycles"].label = "Number Of Cycles"
        self.fields["FinancialInstitution"].label = "Financial Institutions"


    class Meta:
        model = Vsla
        title = "Vsla"
        fields = ["id", "VslaCode", "VslaName", "VslaPhoneMsisdn", "PhysicalAddress", "GpsLocation", "DateRegistered", "DateLinked", "Region", "ContactPerson", "PositionInVsla", "PhoneNumber", "TechnicalTrainer", "Status", "GroupAccountNumber", "NumberOfCycles", "Implementer", "FinancialInstitution"]