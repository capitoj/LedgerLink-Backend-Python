from ledgerlink.models import Meeting
from xf.xf_crud.model_forms import XFModelForm

class MeetingForm(XFModelForm):

    def __init__(self, *args, **kwargs):
        super(MeetingForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Meeting
        title = "VSLA Meeting"
        fields = ["id", "MeetingIdEx", "CashExpenses", "CashFromBox", "CashSavedBank", "CashWelfare", "DateSent", "IsCurrent", "IsDataSent"]