from django.db import models
from django.core.validators import MinLengthValidator

class House(models.Model):
    name = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "House must be greater than 1 character")]
    )

    def __str__(self):
        return self.name

class Wizard(models.Model):
    nickname = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Nickname must be greater than 1 character")]
    )
    power = models.PositiveIntegerField()
    spell = models.CharField(max_length=300)
    house = models.ForeignKey('House', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nickname