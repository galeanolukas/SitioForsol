from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls'), name='login'),
    url(r'^contacto/', views.vista_contacto, name='contacto'),
    url(r'^usuarios/', views.usuarios, name='usuarios'),
    url(r'^posteos/nuevo/', views.post_nuevo, name='postear'),
    url(r'^posteos/editar/(?P<ID>\d+)/$', views.editar_post, name='editar_post'),
    url(r'^posteos/ver/$', views.mostrar_post, name='ver_post'),
    url(r'^posteos/eliminar/(?P<ID>\d+)/$', views.borrar_post, name='eliminar'),
    url(r'^galeria/', views.galeria, name='galeria'),
    url(r'^cargar/', views.cargar_galeria, name='cargar'),
    url(r'^salir/', views.cerrar_sesion, name='salir'),
    url(r'^registro/', views.registro, name='registrar')
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#)