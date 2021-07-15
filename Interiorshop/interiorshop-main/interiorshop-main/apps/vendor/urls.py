from django.contrib.auth import views as auth_views
from django.urls import path,include

from . import views

urlpatterns = [
    path('become-vendor/', views.become_vendor, name='become_vendor'),
    path('vendor-admin/', views.vendor_admin, name='vendor_admin'),
    path('add-product/', views.add_product, name='add_product'),
    path('edit-vendor/', views.edit_vendor, name='edit_vendor'),
    path('edit-customer/', views.edit_customer, name='edit_customer'),
    path('edit-product/<int:pk>/', views.edit_product, name='edit_product'),
  # path('', core.views, name='frontpage'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   # path('login/', auth_views.LoginView.as_view(template_name='vendor/login.html'), name='login'),
    path('login/', views.user_login, name='user_login'),
    path('', views.vendors, name='vendors'),
    path('<int:vendor_id>/', views.vendor, name='vendor'),


      #path('', include('apps.core.urls')),

]