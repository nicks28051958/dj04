from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_kredit, name='create_kredit'),  # Страница для ввода данных
    path('list/', views.list_kredit, name='list_kredit'),  # Страница для отображения данных
]
