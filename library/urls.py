from django.conf.urls import url
from django.views.generic import TemplateView, RedirectView
from django.conf import settings
from django.contrib.auth import views as auth_views

from library.custom_views import ReturnBookView
from library.forms import BookForm, SmallBookForm, SmallBookList, BookList, ReadOnlyBookList, AuthorList, CheckoutList, \
    WideBookForm, BookInstanceList, CheckoutLineList, CheckoutLineForm
from library.models import Book, Author, Category, BookInstance, Library, Client, Checkout, Payment, CheckoutLine
from library.views import XFMasterChildView, BookMasterChildView, AuthorMasterChildView, BookInstanceMasterChildView, \
    CheckoutMasterChildView
from xf.xf_crud.crud_url_builder import XFCrudURLBuilder
from xf.xf_crud.generic_crud_views import XFDetailView
from xf.xf_crud.xf_crud_helpers import crudurl


urlpatterns = []


# CUSTOM URLS
urlpatterns += (url(r'^library/book/(?P<pk>[-\w]+)/return', ReturnBookView.as_view(), name='library_book_return'),)


# ### URL Builders
# XFCrudURLBuilders are helper classes to build URLs. You need one for each model that you want to work with.
book_builder = XFCrudURLBuilder(url_app_name="library", url_model_name="book", model_type=Book)
author_builder = XFCrudURLBuilder(url_app_name="library", url_model_name="author", model_type=Author)
book_instance_builder = XFCrudURLBuilder(url_app_name="library", url_model_name="book-instances", model_type=BookInstance)
checkout_builder = XFCrudURLBuilder(url_app_name="library", url_model_name="checkout", model_type=Checkout)
checkoutline_builder = XFCrudURLBuilder(url_app_name="library", url_model_name="checkoutline", model_type=CheckoutLine, )

# ### RELATED URLs
# This part builds related-URLs, for example a list of books by-author
urlpatterns += [book_builder.get_list_related_url(list_class_type=BookList, url_related_name="by-author", foreign_key_name="author"),]
# List of book-instances by book, so foreign key field 'book' refers to the book-instance class here
urlpatterns += [book_instance_builder.get_list_related_url(url_related_name="by-book", foreign_key_name="book"),]
# List of checkout lines for a checkout
urlpatterns += [checkoutline_builder.get_list_related_url(url_related_name="by-checkout", foreign_key_name="checkout",
                                                          list_class_type=CheckoutLineList),]

# ### MASTER CHILD PAGES
# This part builds the master-child pages. These two classes must be written as part of your app.
# Specify a form class if you want to have a special form on the top of your screen
urlpatterns += [book_builder.get_overview_url(form_class_type=BookForm, view_class_type=BookMasterChildView)]
urlpatterns += [author_builder.get_overview_url(view_class_type=AuthorMasterChildView)]
urlpatterns += [book_instance_builder.get_overview_url(view_class_type=BookInstanceMasterChildView)]
urlpatterns += [checkout_builder.get_overview_url(view_class_type=CheckoutMasterChildView)]


# ### BASIC CRUD Pages
#
urlpatterns += crudurl("library", "book-instances", BookInstance, None, BookInstanceList)
urlpatterns += crudurl("library", "book", Book, BookForm, BookList)
urlpatterns += crudurl("library/view", "book", Book, BookForm, ReadOnlyBookList)
urlpatterns += crudurl("library", "smallbook", Book, SmallBookForm, SmallBookList)
urlpatterns += crudurl("library", "author", Author, None, AuthorList)
urlpatterns += crudurl("library", "category", Category, None)
urlpatterns += crudurl("library", "library", Library, None)
urlpatterns += crudurl("library", "client", Client, None)
urlpatterns += crudurl("library", "checkout", Checkout, None, CheckoutList)
urlpatterns += crudurl("library", "payment", Payment, None)
urlpatterns += crudurl("library", "checkoutline", CheckoutLine, CheckoutLineForm, CheckoutLineList)

