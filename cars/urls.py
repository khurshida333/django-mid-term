from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    # path('add/', views.add_posts,name='add_posts'),
    path('add/', views.AddCarCreateView.as_view(),name='add_cars'),
    # path('edit<int:id>/', views.edit_posts,name='edit_posts'),
    path('edit<int:id>/', views.EditCarUpdateView.as_view(),name='edit_cars'),
    # path('delete<int:id>/', views. delete_posts,name='delete_posts'),
    path('delete<int:id>/', views.CarDeleteView.as_view(),name='delete_cars'),
    path('details<int:id>/', views.DetailCarView.as_view(),name='details_cars'),
    path('buy<int:car_id>/', views.buy_car,name='buy_car'),
]

