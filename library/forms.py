from crispy_forms.helper import FormHelper
from django.core.exceptions import ValidationError

from library.models import Book

from crispy_forms.layout import Layout, Div, Field
from crispy_forms.bootstrap import TabHolder, Tab
from django import forms
from django.core.urlresolvers import reverse

from xf_crud.model_forms import XFModelForm
from xf_crud.model_lists import XFModelList
from xf_crud.xf_classes import XFUIAction, XFActionType


class BookForm(XFModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "publication_date", "category",]
        title = "Book me"

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = "Enter the book's title"
        self.fields['publication_date'].widget.attrs['class'] = "date-field datepicker"
        self.add_javascript("library.js")

        # Example of pre-setting a value self.initial = {'author':'1'}
        # self.fields['author'].widget.attrs['readonly'] = True

        self.helper.layout = Layout(
            TabHolder(
                Tab('Book',
                    Field('title', 'publication_date', )
                    ),
                Tab('Author',
                    Field('author', 'category', )
                    ),
            )
        )


class SmallBookForm(XFModelForm):
    class Meta:
        model = Book
        fields = ["title"]

        title = "Quickly add a book"

    def __init__(self, *args, **kwargs):
        super(SmallBookForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = "Enter the book's title"

    def clean_title(self):
        title = self.cleaned_data['title']
        if title.find("2") >= 0:
            raise forms.ValidationError("Can't have the word 2 in the title when adding a small book.")

        return title


class SmallBookList(XFModelList):
    def __init__(self, model):
        super(SmallBookList, self).__init__(model)
        self.list_field_list = (("title",))
        self.list_description = "List of small books below."
        self.list_title = "Our smallbooks"
        self.list_hint = "Below is a list of the small books that you can borrow."
        self.supported_crud_operations.append('search')
        self.search_field = "title"
        self.preset_filters = {
            '': 'All',
            'recent': 'Only with "Ze"',
        }

    def get_queryset(self, search_string, model, preset_filter, view_kwargs=None):

        if preset_filter == 'recent':
            return Book.objects.filter(title__contains='Ze').filter(title__contains=search_string)
        else:
            return super().get_queryset(search_string, model, preset_filter, view_kwargs)



class BookList(XFModelList):
    def __init__(self, model):
        super(BookList, self).__init__(model)
        self.list_field_list = ("title", "category", "author", "publication_date", "instance_count")
        self.list_description = "List of books below."
        self.list_title = "Our books"
        self.list_hint = "Below is a list of the books that you can borrow."
        self.supported_crud_operations.append('search')
        self.search_field = "title"
        self.add_javascript("library.js")

        # This makes a row clickable action and takes you to the book overview page (where you can see instances)
        self.row_default_action = XFUIAction('overview', 'View books', 'view', use_ajax=False)

        # Sample: create a small book action – creates an extra button
        self.screen_actions.append(XFUIAction('new_small_book', 'Create small book', 'new', url_name='library_smallbook_new'))


class ReadOnlyBookList(BookList):
    def __init__(self, model):
        super(ReadOnlyBookList, self).__init__(model)
        self.supported_crud_operations.remove('delete')
        self.supported_crud_operations.remove('change')
        self.supported_crud_operations.remove('add')

class AuthorList(XFModelList):

    def __init__(self, model):
        super().__init__(model)
        self.row_default_action = XFUIAction('overview', 'View books', 'view', use_ajax=False)