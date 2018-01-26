from django.core.exceptions import ValidationError

from library.models import Book
from xf_crud.generic_forms import XFModelForm, XFModelList

from crispy_forms.layout import Layout, Div, Field
from crispy_forms.bootstrap import  TabHolder, Tab
from django import forms
from django.core.urlresolvers import reverse



class BookForm(XFModelForm):

    class Meta:
        model = Book
        fields = ["title", "author", "publication_date", "category"]

#        # TODO: Make this work
        #widgets = {
        #    'publication_date': forms.SplitDateTimeWidget
        #}


        title = "Booooooooook me"

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = "Enter the book's title"
        self.fields['publication_date'].widget.attrs['class'] = "date-field datepicker"


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

    class Meta:
        list_field_list = (("title",))
        list_description = "List of small books below."
        list_title = "Our smallbooks"
        list_hint = "Below is a list of the small books that you can borrow."
        default_permissions = ('add', 'change', 'delete', 'view')
        search_field = "title"