from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^fossee4/', include("fossee4.urls" , namespace="fossee4")),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
