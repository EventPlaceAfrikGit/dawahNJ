from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('my-admin/', admin.site.urls),
    path('', include('MyApp.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
