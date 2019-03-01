from django.urls import path
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/2.1/topics/http/urls/
urlpatterns = [
    path('', views.MainView.as_view(), name='wizards'),
    path('main/create/', views.WizardCreate.as_view(), name='wizard_create'),
    path('main/<int:pk>/update/', views.WizardUpdate.as_view(), name='wizard_update'),
    path('main/<int:pk>/delete/', views.WizardDelete.as_view(), name='wizard_delete'),
    path('lookup/', views.HouseView.as_view(), name='house_list'),
    path('lookup/create/', views.HouseCreate.as_view(), name='house_create'),
    path('lookup/<int:pk>/update/', views.HouseUpdate.as_view(), name='house_update'),
    path('lookup/<int:pk>/delete/', views.HouseDelete.as_view(), name='house_delete'),
]