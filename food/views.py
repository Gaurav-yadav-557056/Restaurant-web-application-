from decimal import Decimal
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.db import transaction
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from .cart import Cart
from .forms import FoodForm, CheckoutForm
from .models import Category, Food, Order, OrderItem


def home(request):
    featured_foods = Food.objects.filter(available=True)[:6]
    return render(request, "food/home.html", {"featured_foods": featured_foods})


def food_list(request):
    foods = Food.objects.filter(available=True).select_related("category")
    categories = Category.objects.all()
    query = request.GET.get("q", "").strip()
    category_id = request.GET.get("category", "").strip()

    if query:
        foods = foods.filter(name__icontains=query)
    if category_id.isdigit():
        foods = foods.filter(category_id=int(category_id))

    return render(request, "food/food_list.html", {
        "foods": foods,
        "categories": categories,
        "query": query,
        "selected_category": category_id,
    })


def food_detail(request, id):
    food = get_object_or_404(Food, id=id, available=True)
    return render(request, "food/food_detail.html", {"food": food})


@staff_member_required
def add_food(request):
    if request.method == "POST":
        form = FoodForm(request.POST)
        if form.is_valid():
            food = form.save()
            messages.success(request, f"{food.name} was added.")
            return redirect("food_detail", id=food.id)
    else:
        form = FoodForm()
    return render(request, "food/food_form.html", {"form": form, "page_title": "Add food"})


@staff_member_required
def edit_food(request, id):
    food = get_object_or_404(Food, id=id)
    if request.method == "POST":
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            messages.success(request, "Food item updated.")
            return redirect("food_detail", id=food.id)
    else:
        form = FoodForm(instance=food)
    return render(request, "food/food_form.html", {"form": form, "page_title": "Edit food"})


@staff_member_required
@require_POST
def delete_food(request, id):
    food = get_object_or_404(Food, id=id)
    food_name = food.name
    food.delete()
    messages.success(request, f"{food_name} was deleted.")
    return redirect("food_list")


def cart_detail(request):
    cart = Cart(request)
    items, total = cart.items()
    return render(request, "food/cart.html", {
        "items": items, "total": total, "cart_count": cart.count()
    })


@require_POST
def cart_add(request, id):
    food = get_object_or_404(Food, id=id, available=True)
    try:
        quantity = int(request.POST.get("quantity", "1"))
    except (TypeError, ValueError):
        quantity = 1
    if quantity < 1 or quantity > 99:
        messages.error(request, "Quantity must be between 1 and 99.")
        return redirect("food_detail", id=food.id)
    Cart(request).add(food, quantity=quantity)
    messages.success(request, f"{food.name} added to your cart.")
    return redirect("cart_detail")


@require_POST
def cart_update(request, id):
    food = get_object_or_404(Food, id=id)
    try:
        quantity = int(request.POST.get("quantity", "1"))
    except (TypeError, ValueError):
        quantity = 1
    if quantity > 99:
        messages.error(request, "Maximum quantity is 99.")
        return redirect("cart_detail")
    Cart(request).update(food, quantity)
    return redirect("cart_detail")


@require_POST
def cart_remove(request, id):
    food = get_object_or_404(Food, id=id)
    Cart(request).remove(food)
    messages.success(request, f"{food.name} removed from your cart.")
    return redirect("cart_detail")


def checkout(request):
    cart = Cart(request)
    items, total = cart.items()
    if not items:
        messages.info(request, "Your cart is empty.")
        return redirect("food_list")

    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Re-fetch and price from the database; never trust a client-submitted price.
            with transaction.atomic():
                order = form.save(commit=False)
                order.total = Decimal("0.00")
                order.save()
                verified_total = Decimal("0.00")

                for item in items:
                    food = get_object_or_404(Food, id=item["food"].id, available=True)
                    quantity = item["quantity"]
                    OrderItem.objects.create(
                        order=order,
                        food=food,
                        food_name=food.name,
                        unit_price=food.price,
                        quantity=quantity,
                    )
                    verified_total += food.price * quantity

                order.total = verified_total
                order.save(update_fields=["total"])

            cart.clear()
            return redirect("order_success", id=order.id)
    else:
        form = CheckoutForm()

    return render(request, "food/checkout.html", {
        "form": form, "items": items, "total": total
    })


def order_success(request, id):
    order = get_object_or_404(Order.objects.prefetch_related("items"), id=id)
    return render(request, "food/order_success.html", {"order": order})
