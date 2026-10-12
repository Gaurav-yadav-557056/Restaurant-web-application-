from decimal import Decimal
from .models import Food


class Cart:
    """Small session-based cart. Store only food IDs and quantities in session."""

    SESSION_KEY = "cart"

    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get(self.SESSION_KEY, {})

    def add(self, food, quantity=1, replace=False):
        food_id = str(food.id)
        current = self.cart.get(food_id, 0)
        self.cart[food_id] = int(quantity) if replace else int(current) + int(quantity)
        self.save()

    def update(self, food, quantity):
        food_id = str(food.id)
        if int(quantity) <= 0:
            self.remove(food)
        else:
            self.cart[food_id] = int(quantity)
            self.save()

    def remove(self, food):
        self.cart.pop(str(food.id), None)
        self.save()

    def save(self):
        self.session[self.SESSION_KEY] = self.cart
        self.session.modified = True

    def clear(self):
        self.session.pop(self.SESSION_KEY, None)
        self.cart = {}

    def items(self):
        result = []
        total = Decimal("0.00")
        for food_id, quantity in self.cart.items():
            try:
                food = Food.objects.get(id=int(food_id), available=True)
            except (Food.DoesNotExist, ValueError):
                continue
            quantity = int(quantity)
            line_total = food.price * quantity
            total += line_total
            result.append({
                "food": food,
                "quantity": quantity,
                "line_total": line_total,
            })
        return result, total

    def count(self):
        return sum(int(quantity) for quantity in self.cart.values())
