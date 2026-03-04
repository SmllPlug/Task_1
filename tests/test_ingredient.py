import pytest

from praktikum.ingredient import Ingredient
from tests.data import FILLING, SAUCE

class TestIngredient:
    @pytest.mark.parametrize('ingredient_type, name, price', FILLING + SAUCE)
    def test_ingredient_getters(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price