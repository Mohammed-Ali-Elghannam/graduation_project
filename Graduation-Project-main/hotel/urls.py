from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('verify-email/<int:user_id>/<str:token>/', views.verify_email, name='verify_email'),
    path('logout/', views.logout_view, name='logout'),
    path('search/', views.hotel_search, name='hotel_search'),
    path('hotel/<int:pk>/', views.hotel_detail, name='hotel_detail'),  

]