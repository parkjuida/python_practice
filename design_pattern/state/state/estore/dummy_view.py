from rest_framework.views import APIView

from estore.repository import OrderRepository


class OrderState:
    InitOrderState = 'InitOrderState'
    PrepareOrderState = 'PrepareOrderState'
    DeliveryOrderState = 'DeliveryOrderState'


class EstoreDummyView(APIView):
    def get_object(self, pk):
        order = OrderRepository.get(pk)
        return order

    def put(self, request, pk):
        order = self.get_object(pk)
        if order.state == OrderState.InitOrderState:
            order.state = OrderState.PrepareOrderState
            print("This is prepare order state")
        elif order.state == OrderState.PrepareOrderState:
            order.state = OrderState.DeliveryOrderState
            print("This is delivery order state")
        pass
