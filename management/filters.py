import django_filters
from django_filters import FilterSet

from .models import User, Ingredient


class UserFilter(FilterSet):
	class Meta:
		model = User
		fields = ['email']
		
		
class IngredientFilter(FilterSet):
	class Meta:
		model = Ingredient
		fields = ['name']
