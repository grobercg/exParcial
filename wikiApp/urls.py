from django.urls import path
from . import views

app_name='wikiApp'

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('nuevoTema',views.nuevoTema,name='nuevoTema'),
    path('nuevoArticulo',views.nuevoArticulo,name='nuevoArticulo'),
    path('Ingeniería',views.Ingeniería,name='Ingeniería'),
    path('Informática',views.Informática,name='Informática'),
    path('Economía',views.Economía,name='Economía'),
    path('Derecho',views.Derecho,name='Derecho'),
    path('articulos11',views.articulos11,name='articulos11'),
    path('articulos12',views.articulos12,name='articulos12'),
    path('articulos21',views.articulos21,name='articulos21'),
    path('articulos22',views.articulos22,name='articulos22'),
    path('articulos31',views.articulos31,name='articulos31'),
    path('articulos32',views.articulos32,name='articulos32'),
    path('articulos41',views.articulos41,name='articulos41'),
    path('articulos42',views.articulos42,name='articulos42'),
    path('busqueda',views.busqueda,name='busqueda')
]