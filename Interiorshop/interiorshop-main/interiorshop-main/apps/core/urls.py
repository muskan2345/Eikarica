#
#

from django.urls import path

#
#

from . import views
from apps.vendor.views import user_login, user_logout


#
#

urlpatterns = [
    path('', user_login, name='user_login'),
    path('home/', views.frontpage, name='frontpage'),
    path('logout/', user_logout, name='user_logout'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about')
]