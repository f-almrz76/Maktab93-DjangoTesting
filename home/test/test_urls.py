from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import Home, About


# you can use Testcase is not different!!
class TestUrls(SimpleTestCase):
    def test_home(self):
        url = reverse('home:home')  # /
        # print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, Home)

    def test_about(self):
        url = reverse('home:about', args=('fateme',))  # about/fateme
        # print(url)
        # print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, About)
