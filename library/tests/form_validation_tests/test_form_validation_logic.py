import datetime

from library.forms import SmallBookForm
from library.models import Book
from xf.xf_system.testing.xf_test_case import XFTestCase


class ValidateSmallBookForm(XFTestCase):

    def setUp(self):
        super().setUp()
        self.form_data = {}

    def test_title(self):

        self.form_data['title'] = 'Hello 2 shouldn\'t work'
        self.form_data['author'] = 6
        form = SmallBookForm(self.form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
