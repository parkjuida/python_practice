from django.urls import path

from estore import views

urlpatterns = [
    path('', views.EstoreCreateView.as_view()),
    path('<int:pk>', views.EstoreView.as_view()),
]

