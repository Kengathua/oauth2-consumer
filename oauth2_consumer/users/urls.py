from django.urls import path

from rest_framework import routers

from oauth2_consumer.users import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path(r'me/', views.MeView.as_view(), name='user-me'),
    path('home/', views.home, name='secret')
]
