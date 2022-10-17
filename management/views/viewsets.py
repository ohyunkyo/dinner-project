from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status as HttpStatus

from management.filters import UserFilter, IngredientFilter
from management.models import User, Ingredient, IngredientInventory, InventoryLog, Recipe
from management.serializers import UserSerializer, IngredientSerializer, IngredientInventorySerializer, IngredientInventoryCreateSerializer, InventoryLogSerializer, RecipeSerializer


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter
    serializer_class = UserSerializer


class IngredientModelViewSet(ModelViewSet):
    queryset = Ingredient.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = IngredientFilter
    serializer_class = IngredientSerializer


class IngredientInventoryModelViewSet(ModelViewSet):
    queryset = IngredientInventory.objects.all()
    filter_backends = [DjangoFilterBackend]
    serializer_class = IngredientInventorySerializer

    def create(self, request, *args, **kwargs):
        serializer = IngredientInventoryCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)

            return Response(serializer.data, HttpStatus.HTTP_200_OK)
        else:
            return Response(serializer.errors)


class InventoryLogModelViewSet(ModelViewSet):
    queryset = InventoryLog.objects.all()
    filter_backends = [DjangoFilterBackend]
    serializer_class = InventoryLogSerializer


class RecipeModelViewSet(ModelViewSet):
    queryset = Recipe.objects.all()
    filter_backends = [DjangoFilterBackend]
    serializer_class = RecipeSerializer
