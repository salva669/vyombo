from django.urls import path
from vyomboapp import views
from vyombo import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.ShowIndexPage, name='show_index'),
    path('cookware_page', views.ShowCookwarePage, name='cookware_page'),
    path('dinnerware_page', views.ShowDinnerwarePage, name='dinnerware_page'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
