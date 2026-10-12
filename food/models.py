from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=80, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Food(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="foods",
        null=True, blank=True
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(
        max_digits=8, decimal_places=2,
        validators=[MinValueValidator(Decimal("0.01"))]
    )
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = [
        ("PLACED", "Placed"),
        ("PREPARING", "Preparing"),
        ("READY", "Ready"),
        ("COMPLETED", "Completed"),
        ("CANCELLED", "Cancelled"),
    ]

    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    delivery_address = models.TextField()
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default="PLACED")
    total = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Order #{self.pk} — {self.customer_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    food = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True, blank=True)
    # Snapshot values preserve what was ordered even if the food name/price changes later.
    food_name = models.CharField(max_length=100)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def line_total(self):
        return self.unit_price * self.quantity

    def __str__(self):
        return f"{self.food_name} x {self.quantity}"
