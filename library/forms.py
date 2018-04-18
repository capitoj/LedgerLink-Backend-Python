from crispy_forms.helper import FormHelper
from django.core.exceptions import ValidationError
from django.forms import HiddenInput

from library.models import Book, CheckoutLine, Checkout, Author

from crispy_forms.layout import Layout, Div, Field, HTML
from crispy_forms.bootstrap import TabHolder, Tab
from django import forms
from django.core.urlresolvers import reverse, resolve
from django.forms.widgets import TextInput

from xf.xf_crud.model_forms import XFModelForm
from xf.xf_crud.model_lists import XFModelList
from xf.xf_crud.widgets import TypeAheadWidget, StaticTextWidget, StaticSelectWidget, MissingTextInput
from xf.xf_crud.xf_classes import XFUIAction, ACTION_RELATED_INSTANCE, ACTION_ROW_INSTANCE, \
    ACTION_PREINITIALISED_RELATED_INSTANCE


class BookForm(XFModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "publication_date", "category",]
        title = "Book me"
        #widgets = {
        #    'category': TypeAheadWidget
        #}

    #category = forms.TextInput()

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = "Enter the book's title"
        self.fields['publication_date'].widget.attrs['class'] = "date-field datepicker"
        #self.fields['category'] = TextInput()
        #self.fields['category'].widget = forms.TextInput

        self.add_javascript("library.js")

        # Example of pre-setting a value self.initial = {'author':'1'}
        # self.fields['author'].widget.attrs['readonly'] = True

        # An example of how you can use a single form for multiple purposes
        if self.url_name == 'library_book_overview':
            self.helper.layout = Layout(
                Div(
                    Div(HTML(
                        "<p>This is a fully working overview page. The form displayed here is a 'BookForm'</p>"),
                        css_class='col-md-12')
                    , css_class='row'
                ),
                Div(
                    Div('title', 'publication_date', css_class='col-md-4'),
                    Div('author', 'category', css_class='col-md-4'),
                    Div(HTML("Some more text"), css_class='col-md-4'),
                    css_class='row',
            ),
            )
        elif self.url_name != 'library_book_details':
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
        else: # default layout for details form
            pass

class WideBookForm(BookForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.helper.form_class = None
        self.helper.layout = Layout(
            Div(
                Div(HTML("<p>This is a fully working overview page. The form displayed here is a 'WideBookForm'</p>"), css_class='col-md-12')
                , css_class='row'
            ),
            Div(
                Div('title', 'publication_date',css_class='col-md-6'),
                Div('author', 'category', css_class='col-md-6'), css_class='row'
            ),
        )



class SmallBookForm(XFModelForm):
    class Meta:
        model = Book
        fields = ["title", "author"]

        title = "Quickly add a book"

    def __init__(self, *args, **kwargs):
        super(SmallBookForm, self).__init__(*args, **kwargs)
        self.helper.form_class += ' form-static'
        self.fields['title'].widget.attrs['placeholder'] = "Enter the book's title"
        #self.fields['title'].widget = StaticTextWidget()
        #self.fields['author'].widget = StaticSelectWidget(choices=self.fields['author'].choices)
        #widget = self.fields['author'].widget
        #field = self.fields['author']
        #self.fields['author'].widget.template_name = "widgets/static_select.html"



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

        # Sample: This attaches a book overview - the master child view - to the first column
        self.row_action_list.append(XFUIAction('overview', 'View books', 'view', use_ajax=False, column_index=1))

        # Sample: create a small book action – creates an extra button
        self.screen_actions.append(XFUIAction('new_small_book', 'Create small book', 'new', url_name='library_smallbook_new'))

        # Sample: create a new instance
        create_new_instance_action = XFUIAction('new_instance', 'Create book instance', 'new',
                                                url_name='library_book-instances_new',
                                                action_type=ACTION_PREINITIALISED_RELATED_INSTANCE)
        create_new_instance_action.initial_data = "book="
        self.row_action_list.append(create_new_instance_action)

        # Sample: Create a another clickable cell to see the details of a category
        self.row_action_list.append(XFUIAction('category_details', 'See', 'view2', url_name='library_category_details', use_ajax=True,
                           action_type=ACTION_RELATED_INSTANCE, column_index=2))


class ReadOnlyBookList(BookList):
    def __init__(self, model):
        super(ReadOnlyBookList, self).__init__(model)
        self.supported_crud_operations.remove('delete')
        self.supported_crud_operations.remove('change')
        self.supported_crud_operations.remove('add')

class AuthorList(XFModelList):

    def __init__(self, model):
        super().__init__(model)
        self.row_action_list.append(XFUIAction('overview', 'View books', 'view', use_ajax=False, column_index=1))


class AuthorForm(XFModelForm):

    class Meta:
        model = Author
        fields = ['first_name', 'last_name']
        title = "Author"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget = MissingTextInput(is_new_entity=self.is_new_entity(), blank_text="Unknown/declined")
        self.fields['last_name'].widget = MissingTextInput(is_new_entity=self.is_new_entity())

    def prepare_form_for_save(self, instance):

        #instance.first_name = "Always this first name"
        super().prepare_form_for_save(instance)


class CheckoutList(XFModelList):

    def __init__(self, model):
        super().__init__(model)
        #self.supported_crud_operations.remove('change')
        self.get_action('new').next_url = 'library_checkout_details'
        self.get_entity_action('edit').next_url = 'library_checkout_details'
        self.row_action_list.append(XFUIAction('overview', 'Overview', 'view', use_ajax=False, column_index=1))


class BookInstanceList(XFModelList):

    def __init__(self, model):
        super().__init__(model)
        self.row_default_action = XFUIAction('overview', 'Overview', 'view', use_ajax=False)

class CheckoutLineList(XFModelList):

    def __init__(self, model):
        super().__init__(model)
        self.get_action('new').action_caption = "Add book to checkout"
        self.row_action_list.append(XFUIAction('return_book', 'Return book', 'view2', url_name='library_book_return', use_ajax=True,
                           action_type=ACTION_ROW_INSTANCE))


class CheckoutLineForm(XFModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['checkout'].disabled = True
        self.fields['checkout'].widget = HiddenInput()

        # Here is an example where a default value can be set based on the value of
        # another object. We retrieve the Checkout related to this checkoutline and
        # attach the dates of it.
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:    # Editing existing checkout
            self.Meta.title = "Edit book"
            self.fields['checkout_date'].disabled = True
            self.fields['required_checkin_date'].disabled = True
            self.fields['book_instance'].disabled = True
            self.fields['actual_checkin_date'].disabled = False
        else:   # Create a new checkout
            self.fields['actual_checkin_date'].widget = HiddenInput()
            self.fields['actual_checkin_date'].disabled = True
            self.fields['required_checkin_date'].disabled = True

            if 'initial' in kwargs:
                if 'checkout' in kwargs['initial']:
                    checkout_pk = kwargs['initial']['checkout']
                    checkout = Checkout.objects.get(pk=checkout_pk)
                    self.initial['checkout_date'] = checkout.checkout_date
                    self.initial['required_checkin_date'] = checkout.required_checkin_date
                    self.fields['checkout_date'].disabled = True



    class Meta:
        model = CheckoutLine
        fields = ["checkout", "book_instance", "checkout_date", "required_checkin_date", "actual_checkin_date"]
        title = "Add a book to checkout"
