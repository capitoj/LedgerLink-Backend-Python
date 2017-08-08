from library.models import Book
from xf_crud.generic_forms import XFModelForm

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
        #    'enrollment_date': DateTimePicker,
        #}

        title = "Booooooooook me"

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = "Enter the book's title"