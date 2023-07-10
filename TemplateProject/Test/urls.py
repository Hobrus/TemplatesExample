from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('second_page/', views.second_page, name='second_page'),
    path('test_model/', views.MyTestModelView.as_view(), name='test_model'),
]
