from django.urls import path
from . import views
app_name = 'banking_app'
urlpatterns = [
 path('countries/', views.country_list, name='country_list'),
 path('countries/<int:pk>/edit/', views.country_edit, name='country_edit'),
]
Y en `Banking/urls.py` (archivo del proyecto) agrega la inclusión:
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
 path('admin/', admin.site.urls),
 path('', include('authentication_app.urls')),
]
