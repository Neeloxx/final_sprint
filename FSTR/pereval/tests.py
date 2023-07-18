from django.test import TestCase
from .models import User, Pereval, Level, Coords, Image
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.reverse import reverse


def create_pereval(self):
    return Pereval.objects.create(user=self.user, beauty_title='test1', \
                                  title='title_test', other_titles='other_title', \
                                  level=self.level, coords=self.coords, image=self.image)


class ApiModelTest(TestCase):
    def setUp(self):
        # Setup run before every test method.
        self.user = User.objects.create(name='test_name',
                                             fam='test_fam',
                                             otc='test_otc',
                                             email='emailtest@mail.com',
                                             phone='88005553535')
        self.level = Level.objects.create(winter='1')
        self.coords = Coords.objects.create(latitude='1', longitude='1', height='1')
        self.image = Image.objects.create(title='123', image='null')

    def tearDown(self):
        pass

    def test_setUpTestData(self):

        new = create_pereval(self)
        self.assertEqual(new.beauty_title, 'beauty_title_test')


class PersonViewSetTests(APITestCase):

    def test_list_pereval(self):


        url = 'http://127.0.0.1:8000%s' % reverse('list_or_create')

        response = self.client.get(url, format='json')
        json = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(json), 4)