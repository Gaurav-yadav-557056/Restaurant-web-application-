from django.contrib import admin
from .models import Category, Food, Order, OrderItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "available", "created_at")
    list_filter = ("available", "category")
    search_fields = ("name", "description")
    list_editable = ("price", "available")


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ("food", "food_name", "unit_price", "quantity")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer_name", "customer_email", "total", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("customer_name", "customer_email")
    list_editable = ("status",)
    inlines = [OrderItemInline]
