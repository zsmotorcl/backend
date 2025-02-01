import pytest

from zsmotor.crm.models import CarBrand
from zsmotor.crm.models import Location
from zsmotor.crm.models import Warehouse


@pytest.mark.parametrize(
    ("model", "expected"),
    [
        (
            CarBrand,
            'SELECT "TABMR"."KOMR", "TABMR"."NOKOMR" FROM "TABMR"',
        ),
        (
            Location,
            'SELECT "TABSU"."EMPRESA", "TABSU"."KOSU", "TABSU"."NOKOSU" FROM "TABSU"',
        ),
        (
            Warehouse,
            'SELECT "TABCARAC"."KOTABLA", "TABCARAC"."KOCARAC", "TABCARAC"."NOKOCARAC" FROM "TABCARAC" WHERE "TABCARAC"."KOTABLA" = BODEGAS',  # noqa: E501
        ),
    ],
    ids=["car-brands", "locations", "warehouses"],
)
@pytest.mark.disable_socket
def test_queries(model, expected):
    queryset = model.objects.all()
    assert str(queryset.query) == expected
