from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import viewsets

router = DefaultRouter()

router.register(r'user', viewsets.UserModelViewSet, basename='user')


urlpatterns = [
	# api
	path('api/', include(router.urls)),
]