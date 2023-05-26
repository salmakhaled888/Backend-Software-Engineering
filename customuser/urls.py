from django.urls import path, include
from rest_framework.routers import DefaultRouter

from customuser import views

router = DefaultRouter()
router.register('users', views.UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('login/',views.LoginView.as_view())
]