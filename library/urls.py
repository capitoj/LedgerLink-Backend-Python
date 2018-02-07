from django.conf.urls import url
from django.views.generic import TemplateView, RedirectView
from django.conf import settings
from django.contrib.auth import views as auth_views

from library.forms import BookForm, SmallBookForm, SmallBookList, BookList, ReadOnlyBookList
from library.models import Book, Author, Category
from xf_crud.xf_crud_helpers import crudurl


urlpatterns = []
urlpatterns += crudurl("library", "book", Book, BookForm, BookList)
urlpatterns += crudurl("library/view", "book", Book, BookForm, ReadOnlyBookList)
urlpatterns += crudurl("library", "smallbook", Book, SmallBookForm, SmallBookList)
urlpatterns += crudurl("library", "author", Author, None)
urlpatterns += crudurl("library", "category", Category, None)



