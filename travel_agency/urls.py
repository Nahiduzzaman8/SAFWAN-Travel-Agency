from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path("api/tours/", include("tours.urls")),
    path("api/contact/", include("contact.urls")),
]
