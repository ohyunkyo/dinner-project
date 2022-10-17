from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import viewsets

router = DefaultRouter()

router.register(r'user', viewsets.UserModelViewSet, basename='user')
router.register(r'ingredient', viewsets.IngredientModelViewSet, basename='ingredient')
router.register(r'ingredient_inventory', viewsets.IngredientInventoryModelViewSet, basename='ingredient_inventory')
router.register(r'inventory_log', viewsets.InventoryLogModelViewSet, basename='inventory_log')
router.register(r'recipe', viewsets.RecipeModelViewSet, basename='recipe')


urlpatterns = [
	# api
	path('api/', include(router.urls)),
]