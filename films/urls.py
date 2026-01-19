from django.urls import path
from films import views

urlpatterns = [
    path('adminList/', views.admin_list, name='admin_list'),
    path('<int:film_id>/', views.film_detail, name='film_detail'),
    path('delete/<int:film_id>/', views.film_delete, name='film_delete'),
    path('create/', views.film_create, name='film_create'),
    path('update/<int:film_id>/', views.film_update, name='film_update'),
]