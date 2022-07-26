from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import api_views

router = DefaultRouter()

router.register(r'user', api_views.UserModelViewSet, basename='user')


urlpatterns = [
	# api
	path('api/', include(router.urls)),
]