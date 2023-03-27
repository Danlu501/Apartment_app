from django.urls import path

from . import views

app_name = 'lghter'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.EditView.as_view(), name='detail'),
    path('new/', views.NewView.as_view(), name='new'),
    path('edit/<int:pk>/', views.EditView.as_view(), name='edit'),
]