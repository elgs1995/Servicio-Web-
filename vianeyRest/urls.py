from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from vianeyRest import views

urlpatterns = [
    url(r'^persona/$',views.PersonaList.as_view()),
    url(r'^persona/(?P<pk>[0-9]+)/$',views.PersonaDetail.as_view()),
    url(r'^materia/$', views.MateriaList.as_view()),
    url(r'^materia/(?P<pk>[0-9]+)/$', views.MateriaDetail.as_view()),
    url(r'^usuario/$', views.UsuarioList.as_view()),
    url(r'^usuario/(?P<pk>[0-9]+)/$', views.UsuarioDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

