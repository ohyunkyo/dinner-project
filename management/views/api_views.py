from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from management.filters import UserFilter
from management.models import User
from management.serializers import UserSerializer


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter
    serializer_class = UserSerializer
