"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from products.views import home_page, single_product, MyFormView, MyLoginFormView, logout_view, category_page, \
    add_product_to_cart, user_cart, add_favorite, user_favorite
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    #path('search', search_products),
    path('product/<int:id>', single_product),
    path('category/<int:id>', category_page),
    path('register', MyFormView.as_view()),
    path('login', MyLoginFormView.as_view()),
    path('logout', logout_view),
    path('add_to_cart/<int:id>', add_product_to_cart),
    path('user_cart/', user_cart),
    path('add_favorite/<int:id>', add_favorite),
    path('user_favorite/', user_favorite)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
