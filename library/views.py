from django.core.exceptions import PermissionDenied
from django.db.models import ProtectedError
from django.urls import reverse
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from django.views.generic.edit import ModelFormMixin

from library.models import BookInstance
from xf_crud.ajax_mixins import XFAjaxViewMixin
from xf_crud.generic_crud_views import XFDetailView, XFMasterChildView
from xf_crud.mixins import XFCrudMixin
from xf_crud.model_lists import XFModelList, XFDivLoader
from xf_crud.permission_mixin import XFPermissionMixin
from xf_system.views import XFNavigationViewMixin


class BookMasterChildView(XFMasterChildView):
    template_name = "form_master_child.html"

    def get_context_data(self, **kwargs):
        context = super(BookMasterChildView, self).get_context_data(**kwargs)

        book_instances = XFDivLoader()
        book_instances.caption = "Some of the instances";
        book_instances.url = reverse('library_book-instances_list_by-book', kwargs={'related_fk':self.kwargs['pk']}) + "?&embed"
        self.add_related_listview(book_instances)

        widget = XFDivLoader()
        widget.caption = "Statistics"
        widget.url = "http://127.0.0.1:8001/widgets/mean-bruto/"
        self.add_related_listview(widget)

        return context

class AuthorMasterChildView(XFMasterChildView):
    template_name = "form_master_child.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        books = XFDivLoader()
        books.caption = "Books written"
        books.url = reverse('library_book_list_by-author', kwargs={'related_fk':self.kwargs['pk']}) + "?&embed"
        self.add_related_listview(books)
        return context




