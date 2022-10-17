from rest_framework import serializers

from .models import User, Ingredient, IngredientInventory, InventoryLog, Recipe


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'email', 'password']


class IngredientSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ingredient
		fields = ['id', 'name']


class IngredientInventoryCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = IngredientInventory
		fields = ['id', 'ingredient', 'detail', 'unit']


class IngredientInventorySerializer(serializers.ModelSerializer):
	class Meta:
		model = IngredientInventory
		fields = ['id', 'ingredient', 'user', 'detail', 'unit']


class InventoryLogSerializer(serializers.ModelSerializer):
	class Meta:
		model = InventoryLog
		fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Recipe
		fields = '__all__'
