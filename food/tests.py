from django.test import TestCase
from django.urls import reverse
from .models import Category, Food


class RestaurantBasicTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Main Course")
        self.food = Food.objects.create(
            category=self.category,
            name="Pizza",
            description="Cheese pizza",
            price="250.00",
            available=True,
        )

    def test_home_page_loads(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_food_list_shows_available_food(self):
        response = self.client.get(reverse("food_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Pizza")

    def test_missing_food_returns_404(self):
        response = self.client.get(reverse("food_detail", args=[99999]))
        self.assertEqual(response.status_code, 404)
