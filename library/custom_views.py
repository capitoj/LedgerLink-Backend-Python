from django.http import Http404
from django.urls import reverse
from django.views.generic import TemplateView, FormView

from library.models import CheckoutLine
from xf.xf_crud.ajax_mixins import XFAjaxViewMixin
from xf.xf_system.views import XFNavigationViewMixin
from random import *


class ReturnBookView(TemplateView, XFAjaxViewMixin, XFNavigationViewMixin):

    # Create a template for this view
    template_name = "return_book.html"
    ajax_template_name = "return_book.html"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.return_book_fail = False  # A variable that keeps track of whether our operation succeeded
        self.success_message = "The book has successfully been returned."  # Custom conformation message

    def get_context_data(self, **kwargs):
        context = self.context = super().get_context_data(**kwargs)

        # Make sure that the AJAX template gets loaded
        if self.xf_is_ajax():
            context['ajax'] = True

        try:
            check_out_line = CheckoutLine.objects.get(pk=kwargs['pk'])
            context["book_title"] = check_out_line.book_instance.book.title
        except CheckoutLine.DoesNotExist:
            raise Http404
        except ValueError:
            raise Http404

        # Pass the success or failure of our operation to the template
        context["return_book_fail"] = self.return_book_fail
        context['url_name_list'] = 'library_book_list'

        # This is used for non-AJAX requests. It determines where to go next
        # on a successful submission (no errors)
        # In this case, we're returning the user to the check out overview page
        # of which this CheckOutLineItem belongs
        # For AJAX it is not necessary
        # To code defensively, set it anyway
        context['next_url'] = reverse("library_checkout_overview", args=(kwargs['pk'],))
        self.set_navigation_context()
        return context

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        # Do your logic here
        # This is pseudo logic
        random_number = randint(1, 2)
        if random_number == 1:
            # simulate a fail
            self.return_book_fail = True

        # Set the success variable to be sent back via AJAX
        self.success = not self.return_book_fail

        # Wrap your response in a JSON response and send it back
        # Or, if not AJAX, redirect to next_url
        return self.prepare_ajax_post_response(**kwargs)
