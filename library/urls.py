from django.conf.urls import url
from django.views.generic import TemplateView, RedirectView
from django.conf import settings
from django.contrib.auth import views as auth_views

from library.forms import BookForm, SmallBookForm, SmallBookList, BookList, ReadOnlyBookList
from library.models import Book, Author, Category, BookInstance, Library
from library.views import XFMasterChildView, BookMasterChildView, AuthorMasterChildView
from xf_crud.crud_url_builder import XFCrudURLBuilder
from xf_crud.generic_crud_views import XFDetailView
from xf_crud.xf_crud_helpers import crudurl


urlpatterns = []

# ### URL Builders
# XFCrudURLBuilders are helper classes to build URLs. You need one for each model that you want to work with.
book_builder = XFCrudURLBuilder(url_app_name="library", url_model_name="book", model_type=Book)
author_builder = XFCrudURLBuilder(url_app_name="library", url_model_name="author", model_type=Author)
book_instance_builder = XFCrudURLBuilder(url_app_name="library", url_model_name="book-instances", model_type=BookInstance)

# ### RELATED URLs
# This part builds related-URLs, for example a list of books by-author
urlpatterns += [book_builder.get_list_related_url(list_class_type=BookList, url_related_name="by-author", foreign_key_name="author"),]
# List of book-instances by book, so foreign key field 'book' refers to the book-instance class here
urlpatterns += [book_instance_builder.get_list_related_url(url_related_name="by-book", foreign_key_name="book"),]

# ### MASTER CHILD PAGES
# This part builds the master-child pages. These two classes must be written as part of your app.
urlpatterns += [book_builder.get_overview_url(view_class_type=BookMasterChildView)]
urlpatterns += [author_builder.get_overview_url(view_class_type=AuthorMasterChildView)]

# ### BASIC CRUD Pages
#
urlpatterns += crudurl("library", "book-instances", BookInstance, None)
urlpatterns += crudurl("library", "book", Book, BookForm, BookList)
urlpatterns += crudurl("library/view", "book", Book, BookForm, ReadOnlyBookList)
urlpatterns += crudurl("library", "smallbook", Book, SmallBookForm, SmallBookList)
urlpatterns += crudurl("library", "author", Author, None)
urlpatterns += crudurl("library", "category", Category, None)
urlpatterns += crudurl("library", "library", Library, None)
