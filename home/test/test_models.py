from django.test import TestCase
from home.models import Writer
from model_bakery import baker


class TestWriterModel(TestCase):

    def setUp(self) :
        self.writer = baker.make(Writer, first_name='fateme', last_name='alimirzaei')

    def test_model_str(self):
        #writer = baker.make(Writer, first_name='fateme', last_name='alimirzaei')
        #print(writer.country)
        #writer = Writer.objects.create(first_name='fateme', last_name='alimirzaei', email='fateme@email.com',country='Iran')
       # self.assertEqual(str(writer), 'fateme alimirzaei')
        self.assertEqual(str(self.writer), 'fateme alimirzaei')

