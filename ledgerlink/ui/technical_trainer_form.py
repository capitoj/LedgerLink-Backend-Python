from ledgerlink.models import TechnicalTrainer
from xf.xf_crud.model_forms import XFModelForm

class TechnicalTrainerForm(XFModelForm):

    def __init__(self, *args, **kwargs):
        super(TechnicalTrainerForm, self).__init__(*args, **kwargs)
        self.fields["PhoneNumber"].label = "Phone Number"
        self.fields["FirstName"].label = "First Name"
        self.fields["LastName"].label = "Last Name"
        self.fields["PassKey"].label = "Password"

    class Meta:
        model = TechnicalTrainer
        title = "Community Based Trainer"
        fields = ["id", "Region", "PhoneNumber", "Email", "Status", "FirstName", "LastName", "Username", "PassKey"]