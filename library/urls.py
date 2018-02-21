from django.conf.urls import url
from django.views.generic import TemplateView, RedirectView
from django.conf import settings
from django.contrib.auth import views as auth_views

from library.forms import BookForm, SmallBookForm, SmallBookList, BookList, ReadOnlyBookList
from library.models import Book, Author, Category, BookInstance, Library
from library.views import XFMasterChildView
from xf_crud.crud_url_builder import XFCrudURLBuilder
from xf_crud.xf_crud_helpers import crudurl


urlpatterns = []

book_builder = XFCrudURLBuilder(url_app_name="library", url_model_name="book", model_type=Book)
book_instance_builder = XFCrudURLBuilder(url_app_name="library", url_model_name="book-instances", model_type=BookInstance)
urlpatterns += [book_builder.get_list_related_url(list_class_type=BookList, url_related_name="by-author", foreign_key_name="author"),]
urlpatterns += [book_instance_builder.get_list_related_url(url_related_name="by-book", foreign_key_name="book"),]



urlpatterns += [url(r'^%s/%s/(?P<pk>[-\w]+)/overview' % ("library", "book"),
                   XFMasterChildView.as_view(model=Book, form_class=BookForm,
                                             success_url="%s/%s/" % ("library", "book"), app_name="library",
                                             model_url_part="book"), name="%s_%s_overview" % ("library", "book")),]


urlpatterns += crudurl("library", "book-instances", BookInstance, None)
urlpatterns += crudurl("library", "book", Book, BookForm, BookList)
urlpatterns += crudurl("library/view", "book", Book, BookForm, ReadOnlyBookList)
urlpatterns += crudurl("library", "smallbook", Book, SmallBookForm, SmallBookList)
urlpatterns += crudurl("library", "author", Author, None)
urlpatterns += crudurl("library", "category", Category, None)
urlpatterns += crudurl("library", "library", Library, None)





pass


