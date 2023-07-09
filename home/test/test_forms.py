from django.test import TestCase
from home.forms import UserRegistrationForm
from django.contrib.auth.models import User


class TestRegistrationForm(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username='Elahe', email='Elahe@email.com', password='Elahe')
    def test_valid_data(self):
        form = UserRegistrationForm(data={'username': 'fateme', 'email': 'fateme@gmail.com', 'password1': 'fatemepass',
                                          'password2': 'fatemepass'})
        self.assertTrue(form.is_valid())

    def test_empty_data(self):
        form = UserRegistrationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors) , 4)

    def test_exist_email(self):
       # User.objects.create_user(username='Elahe',email='Elahe@email.com',password='Elahe')
        form = UserRegistrationForm(data={'username': 'NOTElahe', 'email': 'Elahe@email.com', 'password1': 'Elahepass','password2':'Elahepass'})
        self.assertEqual(len(form.errors),1)
        self.assertTrue(form.has_error('email'))

    def test_unmatched_passwords(self):
        form = UserRegistrationForm(data={'username': 'amir', 'email': 'amir@email.com', 'password1': 'amir','password2':'amirrrr'})
        self.assertEqual(len(form.errors),1)
        self.assertTrue(form.has_error)