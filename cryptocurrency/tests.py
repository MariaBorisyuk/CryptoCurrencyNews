from django.test import TestCase, Client
from .models import CryptoCurrency
from .forms import AddCryptocurrencyForm

# Create your tests here.
class AddCryptocurrencyTestCase(TestCase):

    def test_add_cryptocurrency_correct(self):
        client = Client()
        responce = client.post('/add_cryptocurrency/', {'name': 'BTC'})
        self.assertEqual(responce.status_code, 302)
        self.assertEqual(responce.url, '/')
        self.assertEqual(CryptoCurrency.objects.count(), 1)
        self.assertEqual(CryptoCurrency.objects.first().name, 'BTC')

    def test_add_cryptocurrency_inccorect(self):
        client = Client()
        responce = client.post('/add_cryptocurrency/', {'name': 'B-C6'})
        self.assertEqual(responce.status_code, 200)
        self.assertEqual(CryptoCurrency.objects.count(), 0)
        self.assertContains(responce, f'Name of crypto currency must consist of letters:B-C6')

    def test_get_add_cryptocurrency_page(self):
        client = Client()
        responce = client.get('/add_cryptocurrency/')
        form = AddCryptocurrencyForm()
        self.assertContains(responce, str(form))

