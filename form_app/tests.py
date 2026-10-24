from django.test import TestCase
from django.urls import reverse
from .models import Product


class CreateProductTests(TestCase):
    def test_get_renders_product_form(self):
        response = self.client.get(reverse('create_product'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_for.html')

    def test_invalid_post_rerenders_form_with_errors(self):
        response = self.client.post(reverse('create_product'), {'name': 'Widget'})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_for.html')
        self.assertTrue(response.context['form'].errors)

    def test_valid_post_saves_product_and_redirects(self):
        response = self.client.post(
            reverse('create_product'),
            {'name': 'Widget', 'description': '', 'price': '12.50'},
        )

        self.assertRedirects(response, reverse('create_product'))
        self.assertTrue(Product.objects.filter(name='Widget').exists())
