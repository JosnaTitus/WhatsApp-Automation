from django.urls import path

from . import views

urlpatterns = [
  path('accounts/', views.AccountListView.as_view()),
  path('accounts/<int:id>/', views.AccountListView.as_view()),
]