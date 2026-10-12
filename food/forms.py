from django import forms
from .models import Food, Order


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ["category", "name", "description", "price", "available"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3}),
        }


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["customer_name", "customer_email", "delivery_address"]
        widgets = {
            "delivery_address": forms.Textarea(attrs={"rows": 3}),
        }
