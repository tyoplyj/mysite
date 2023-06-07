from django.contrib.auth import login
from django.urls import path, re_path
from django.contrib.auth.views import LoginView
from .templatetags.shop_tags import register
from .views import *
from django.views.decorators.cache import cache_page



urlpatterns = [
    path('', ShopHome.as_view(), name='home'),
    path('about', about, name='about'),
    path('contact', ContactFormView.as_view(), name='contact'),
    path('addproduct/', AddProduct.as_view(), name='addproduct'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/',  RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', cache_page(10)(ShowPost.as_view()), name='post'), # кэш на 10сек
    path('category/<slug:cat_slug>/', ShopCategory.as_view(), name='category'),

]

















