from django.urls import path
from expense import views

urlpatterns = [
   path('get-transactions/', views.get_transactions),
   path("all-transactions/", views.RecordCreation.as_view()),
   path('login/', views.LoginApi.as_view())
]
