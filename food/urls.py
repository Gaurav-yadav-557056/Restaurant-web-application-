from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("food/", views.food_list, name="food_list"),
    path("food/add/", views.add_food, name="add_food"),
    path("food/<int:id>/edit/", views.edit_food, name="edit_food"),
    path("food/<int:id>/delete/", views.delete_food, name="delete_food"),
    path("food/<int:id>/", views.food_detail, name="food_detail"),
    path("cart/", views.cart_detail, name="cart_detail"),
    path("cart/add/<int:id>/", views.cart_add, name="cart_add"),
    path("cart/update/<int:id>/", views.cart_update, name="cart_update"),
    path("cart/remove/<int:id>/", views.cart_remove, name="cart_remove"),
    path("checkout/", views.checkout, name="checkout"),
    path("orders/<int:id>/success/", views.order_success, name="order_success"),
]
