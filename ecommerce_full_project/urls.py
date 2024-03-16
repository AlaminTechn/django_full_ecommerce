from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path, include

def homePage():
    return HttpResponseRedirect('/admin')


urlpatterns = [
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_FOLDER, document_root=settings.MEDIA_ROOT)
