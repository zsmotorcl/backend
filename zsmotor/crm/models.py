from django.conf import settings
from django.db import models


class BaseRandomManager(models.Manager):
    def get_queryset(self):
        # Override the default queryset to use a different database
        return super().get_queryset().using(settings.CRM_DATABASE)


class BaseRandomCRMModel(models.Model):
    # managers
    objects = BaseRandomManager()

    class Meta:
        abstract = True

    def __str__(self):
        return " | ".join(
            [
                getattr(self, field.name).strip()
                for field in self._meta.model._meta.fields  # noqa: SLF001
            ],
        )


class CarBrand(BaseRandomCRMModel):
    name = models.CharField(db_column="KOMR", primary_key=True)
    description = models.CharField(db_column="NOKOMR")

    class Meta:
        managed = False
        db_table = "TABMR"


class Location(BaseRandomCRMModel):
    company = models.CharField(db_column="EMPRESA")
    code = models.CharField(db_column="KOSU", primary_key=True)
    name = models.CharField(db_column="NOKOSU")

    class Meta:
        managed = False
        db_table = "TABSU"


class WarehouseManager(BaseRandomManager):
    def get_queryset(self):
        return super().get_queryset().filter(identifier="BODEGAS")


class Warehouse(BaseRandomCRMModel):
    identifier = models.CharField(db_column="KOTABLA")
    code = models.CharField(db_column="KOCARAC", primary_key=True)
    name = models.CharField(db_column="NOKOCARAC")

    # managers
    objects = WarehouseManager()

    class Meta:
        managed = False
        db_table = "TABCARAC"
