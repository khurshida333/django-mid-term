from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'homepage'),
    path('brand/<slug:brand_slug>/', views.home, name = 'brand_wise_car'),
    path('car_user/', include('car_user.urls')),
    path('brands/', include('brands.urls')),
    path('cars/', include('cars.urls')),

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
