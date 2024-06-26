from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('start', views.start, name='start'),
    path('kategoria/', views.kategoria, name='kategorie'),
    path('uslugi/<int:pk>/', views.uslugi, name='uslugi'),
    path('kategoria/new/', views.kategoria_new, name='kategoria_new'),
    path('kategoria/<int:pk>/edit/', views.kategoria_edit, name='kategoria_edit'),
    path('kategoria/<int:pk>/delete/', views.kategoria_delete, name='kategoria_delete'),
    path('usluga/new/', views.usluga_new, name='usluga_new'),
    path('usluga/<int:pk>/edit/', views.usluga_edit, name='usluga_edit'),
    path('usluga/<int:pk>/delete/', views.usluga_delete, name='usluga_delete'),
    path('klient/', views.klient, name='klient'),
    path('klient/<int:pk>/', views.klient_detail, name='klient_detail'),
    path('klient/new/', views.klient_new, name='klient_new'),
    path('klient/<int:pk>/edit/', views.klient_edit, name='klient_edit'),
    path('klient/<int:pk>/delete/', views.klient_delete, name='klient_delete'),
    path('sprzedawca/', views.sprzedawca, name='sprzedawca'),
    path('sprzedawca/<int:pk>/', views.sprzedawca_detail, name='sprzedawca_detail'),
    path('sprzedawca/new/', views.sprzedawca_new, name='sprzedawca_new'),
    path('sprzedawca/<int:pk>/edit/', views.sprzedawca_edit, name='sprzedawca_edit'),
    path('sprzedawca/<int:pk>/delete/', views.sprzedawca_delete, name='sprzedawca_delete'),
    path('faktura/', views.faktura, name='faktura'),
    path('faktura/<int:pk>/', views.faktura_detail, name='faktura_detail'),
    path('faktura/new/', views.faktura_new, name='faktura_new'),
    path('faktura/<int:pk>/edit/', views.faktura_edit, name='faktura_edit'),
]
