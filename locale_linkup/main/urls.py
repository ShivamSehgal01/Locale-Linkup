from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from main import views
from .views import *

urlpatterns = [
    path('', views.index, name="home"),
    path('seller_index', views.seller_index, name="seller_index"),
    path('customer_index', views.customer_index, name="customer_index"),
    path('product/<int:product_id>/',views.product, name='product'),
    path('add_product/', avatarView, name = 'image_upload'),
    path('login',views.login_page, name="login"),
    path('logout', views.logout_page, name='logout'),
    path('signup',views.signup_page, name="signup"),
    path('seller_signup', views.seller_signup, name="seller_signup"),
    path('customer_signup', views.customer_signup, name="customer_signup"),
    
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)