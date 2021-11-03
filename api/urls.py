from django.urls import path

from . import views


urlpatterns = [
    path('add/<int:a>/<int:b>/', views.add, name='add'),
    path('subtract/<int:a>/<int:b>/', views.subtract, name='subtract'),
    path('multiply/<int:a>/<int:b>/', views.multiply, name='multiply'),
    path('divide/<int:a>/<int:b>/', views.divide, name='divide'),
]
