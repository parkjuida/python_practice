import inspect
import sys
from abc import ABC, abstractmethod


class Order:
    def __init__(self, _id=None, state=None):
        self.id = _id
        self.state = dict(inspect.getmembers(sys.modules[__name__]))[state]()
        if not self.state:
            self.state = InitOrderState()

    def next_state(self):
        self.state.update(self)

    def fail_state(self):
        self.state.fail(self)

    def cancel(self):
        self.state.cancel(self)


class OrderState(ABC):
    @abstractmethod
    def update(self, order):
        pass

    def fail(self, order):
        pass

    def cancel(self, order):
        order.state = CancelOrderState()


class InitOrderState(OrderState):
    def __init__(self):
        print("This is init order state")

    def update(self, order):
        order.state = PrepareOrderState()


class PrepareOrderState(OrderState):
    def __init__(self):
        print("This is prepare order state")

    def update(self, order):
        order.state = DeliveryOrderState()


class DeliveryOrderState(OrderState):
    def __init__(self):
        print("this is delivery order state")

    def update(self, order):
        order.state = CompleteOrderState()


class CancelOrderState(OrderState):
    def __init__(self):
        print("This is cancel order state")

    def update(self, order):
        pass


class CompleteOrderState(OrderState):
    def __init__(self):
        print("This is complete order state")

    def update(self, order):
        pass
