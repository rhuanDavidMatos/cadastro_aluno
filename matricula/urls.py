from django.urls import path
from .views import matricular

urlpatterns = [
    path('matricular/<id>/', matricular, name="matricular"),
]