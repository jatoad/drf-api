from django.urls import path
from items import views

urlpatterns = [
    path('items/', views.ItemList.as_view()),
    # path('drawers/<int:pk>/', views.DrawerDetail.as_view())
]