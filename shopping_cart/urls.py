from django.urls import path
from .views import CartProductView

urlpatterns = [
    path('items/',  CartProductView.as_view()),
    path('items/<int:id>', CartProductView.as_view()),

]
