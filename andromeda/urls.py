from django.urls import path
from . import views

app_name= 'andromeda'

urlpatterns = [
    path('', views.index, name='index'),
    path('producto/<int:producto_id>/', views.producto, name='producto')
]