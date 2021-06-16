from django.http import HttpResponse

from rest_framework.views import APIView

from estore.domains import Order
from estore.repository import OrderRepository


class EstoreCreateView(APIView):
    def post(self, request):
        OrderRepository.create()
        return HttpResponse('success', status=200)


class EstoreView(APIView):
    def get_object(self, pk):
        order = OrderRepository.get(pk)
        return order

    def get(self, request, pk):
        order = self.get_object(pk)
        return HttpResponse(f"{order.id} {order.state.__class__.__name__}")

    def put(self, request, pk):
        order: Order = self.get_object(pk)
        order.next_state()
        OrderRepository.save(order)
        return HttpResponse(f"{order.id} {order.state.__class__.__name__}")

    def delete(self, request, pk):
        order: Order = self.get_object(pk)
        order.cancel()
        OrderRepository.save(order)
        return HttpResponse(f"{order.id} {order.state.__class__.__name__}")
