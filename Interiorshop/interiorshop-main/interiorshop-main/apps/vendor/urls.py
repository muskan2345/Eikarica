from django.contrib.auth import views as auth_views
from django.urls import path,include
from apps.core.views import frontpage
from . import views

urlpatterns = [
    path('become-vendor/', views.become_vendor, name='become_vendor'),
    path('vendor-admin/', views.vendor_admin, name='vendor_admin'),
    path('add-product/', views.add_product, name='add_product'),
    path('edit-vendor/', views.edit_vendor, name='edit_vendor'),
    path('edit-customer/', views.edit_customer, name='edit_customer'),
    path('edit-product/<int:pk>/', views.edit_product, name='edit_product'),
    path('delete-product/<int:pk>/', views.delete_product, name='delete_product'),
    # path('', frontpage, name='frontpage'),
    path('logout/', views.user_logout, name='user_logout'),
   # path('login/', auth_views.LoginView.as_view(template_name='vendor/login.html'), name='login'),
    path('login/', views.user_login, name='user_login'),
    path('', views.vendors, name='vendors'),
    path('<int:vendor_id>/', views.vendor, name='vendor'),
    path('vendor-admin/home/', frontpage, name='frontpage'),
    path('vendor-kyc/', views.vendor_kyc, name='vendor_kyc'),



      #path('', include('apps.core.urls')),

]