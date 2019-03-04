from ledgerlink.models import VslaRegion
from xf.xf_crud.model_forms import XFModelForm


class VslaRegionForm(XFModelForm):

    def __init__(self, *args, **kwargs):
        super(VslaRegionForm, self).__init__(*args, **kwargs)
        self.fields["RegionCode"].label = "Region Code"
        self.fields["RegionName"].label = "Region Name"

    class Meta:
        model = VslaRegion
        title = "Vsla Regions"
        fields = ["id", "RegionCode", "RegionName"]