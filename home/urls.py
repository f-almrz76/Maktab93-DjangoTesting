from django.urls import path

from .views import Home, About, UserRegisterView , WriterView

app_name = "home"

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/<str:username>', About.as_view(), name='about'),
    path('register/',UserRegisterView.as_view(),name='user_register'),
    path('writers/', WriterView.as_view(),name='writers' ),
]
