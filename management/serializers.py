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


class InventoryLogCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = InventoryLog
		fields = ['ingredient_inventory', 'recipe', 'quantity', 'process_name', 'is_increased']


class InventoryLogSerializer(serializers.ModelSerializer):
	class Meta:
		model = InventoryLog
		fields = '__all__'


class RecipeCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Recipe
		fields = ['name', 'ingredients', 'methods']


class RecipeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Recipe
		fields = '__all__'
