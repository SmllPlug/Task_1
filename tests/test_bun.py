import pytest


from praktikum.bun import Bun
from tests.data import BUN

class TestBun:
    @pytest.mark.parametrize('name, price', BUN)
    def test_bun_getters(self, name, price):
        bun = Bun(name, price)

        assert bun.get_name() == name
        assert bun.get_price() == price