from django.urls import path
from drawers import views

urlpatterns = [
    path('drawers/', views.DrawerList.as_view()),
]