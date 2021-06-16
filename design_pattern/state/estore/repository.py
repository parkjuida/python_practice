from estore.domains import InitOrderState, Order as OrderDomain
from estore.models import Order


class OrderRepository:
    @staticmethod
    def get(id):
        order = Order.objects.get(id=id)
        return OrderDomain(order.id, order.state)

    @staticmethod
    def save(order):
        order_object = Order.objects.get(id=order.id)
        order_object.state = order.state.__class__.__name__
        order_object.save()

    @staticmethod
    def create():
        return Order.objects.create(state=InitOrderState.__name__)
