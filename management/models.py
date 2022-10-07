from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db import models


class User(AbstractBaseUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = 'auth_user'
        verbose_name = '사용자'


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    ingredients = models.JSONField()
    methods = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)


class Ingredient(models.Model):
    name = models.CharField(max_length=32, unique=True)


class IngredientInventory(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    detail = models.CharField(max_length=16, null=True, blank=True)
    unit = models.CharField(max_length=16)


class InventoryLog(models.Model):
    ingredient_inventory = models.ForeignKey(IngredientInventory, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.PROTECT, null=True, blank=True)
    quantity = models.IntegerField()
    method = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
