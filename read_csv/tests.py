from django.test import TestCase
from django.urls import reverse


class ReadCsvTest(TestCase):

    def test_incorrect_type(self):
        url = reverse('reader', args=['qwerty'])
        response = self.client.get(url)
        self.assertEqual(response.data, {
            'path': 'qwerty',
            'result': 'Incorrect type of data'
        })

    def test_file_not_exist(self):
        url = reverse('reader', args=['qwerty.xslx'])
        response = self.client.get(url)
        self.assertEqual(response.data, {
            'path': 'qwerty.xslx',
            'result': 'File not found'
        })

    def test_successful_reading(self):
        path = 'https://raw.githubusercontent.com/aniruddhachoudhury/Red-Wine-Quality/master/winequality-red.csv'
        url = reverse('reader',
                      args=['wine.csv'])
        response = self.client.get(url)
        self.assertEqual(response.data, {
            'path': path,
            'result': path + ' readed'
        })
