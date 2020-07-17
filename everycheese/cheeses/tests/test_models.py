import pytest

pytestmark = pytest.mark.django_db

from ..models import Cheese
from .factories import CheeseFactory


def test___str__():
    # cheese = Cheese.objects.create(
    #     name="Stracchino",
    #     description="Semi-sweet cheese that goes well with starches.",
    #     firmness=Cheese.Firmness.SOFT,
    # )
    # assert cheese.__str__() == "Stracchino"
    # assert str(cheese) == "Stracchino"

    def test__str__():
        cheese = CheeseFactory()
        assert cheese.__str__() == cheese.name
        assert str(cheese) == cheese.name
