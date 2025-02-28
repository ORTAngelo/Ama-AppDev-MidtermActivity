from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='login'), 
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('home/', views.home, name='home'),
    path('product/',views.product_list, name='product'),
    path('addProduct/',views.add_product, name='addProduct'),
    path('updateProduct/<int:pk>/',views.update_product, name='updateProduct'),
    path('deleteProduct/<int:pk>/',views.delete_product, name='deleteProduct'),
    path('deleteProduct/<int:pk>/confirm/', views.confirm_delete, name='confirmDelete'),
]