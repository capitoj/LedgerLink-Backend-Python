from django.core.exceptions import PermissionDenied
from django.db.models import ProtectedError
from django.urls import reverse
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from django.views.generic.edit import ModelFormMixin

from xf_crud.ajax_mixins import XFAjaxViewMixin
from xf_crud.generic_crud_views import XFDetailView
from xf_crud.mixins import XFCrudMixin
from xf_crud.permission_mixin import XFPermissionMixin
from xf_system.views import XFNavigationViewMixin


class XFMasterChildView(XFDetailView):
    template_name = "form_master_child.html"

    def get_context_data(self, **kwargs):
        context = super(XFMasterChildView, self).get_context_data(**kwargs)
        context['list_url'] = reverse('library_book-instances_list_related', kwargs={'related_fk':self.kwargs['pk']})
        return context



