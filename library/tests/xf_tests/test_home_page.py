from django.conf import settings
from django.test import TestCase, SimpleTestCase


class MyTestCase(TestCase):

    fixtures = ['test_home_page.json']


    def test_normal_user_account_login(self):

        with self.settings(HOME_PAGE='/somerandomhomepage/'):
            self.client.login(username='normal_user', password='!2345678')
            response = self.client.get('/')
            self.assertTrue(response.wsgi_request.user.is_authenticated())
            self.client.logout()

    def test_normal_user_account_login_with_wrong_password(self):

        self.client.login(username='normal_user', password='!23456789')
        response = self.client.get('/')
        self.assertFalse(response.wsgi_request.user.is_authenticated())
        self.client.logout()
        #self.assertEqual(response.status_code, 200)

    def test_redirect_to_login_page(self):

        login_url = '/log_me_in/'
        with self.settings(LOGIN_URL=login_url):
            response = self.client.get('/')
            self.assertEqual(response.status_code, 302)
            home_page_url = response.url
            response = self.client.get(home_page_url)
            self.assertEqual(response.status_code, 302)
            redirect_to_login_url = response.url
            self.assertEqual("%s?next=%s" % (login_url, settings.HOME_PAGE), redirect_to_login_url)

    def test_home_page_for_normal_user_without_perspective(self):

        # Scenario:
        # A non-super user who is not assigned to a perspective
        # The normal home page should produce a 403, as it includes a perspective slug,
        # and the user does not have a perspective assigned
        self.client.login(username='normal_user', password='!2345678')
        response = self.client.get('/')
        home_page_url = response.url
        self.assertEqual(settings.HOME_PAGE, home_page_url)
        response = self.client.get(home_page_url)
        self.assertEqual(response.status_code, 403)
