from django.db import models

# Create your models here.
class FoodLog(models.Model):
    title=models.CharField(max_length=200)

    calories=models.CharField(max_length=200)

    MEAL_TYPE_CHOICES=(
        ("breakfast","breakfast"),
        ("lunch","lunch"),
        ("dinner","dinner"),
        ("snacks","snacks")
    )

    meal_type=models.CharField(max_length=200,choices=MEAL_TYPE_CHOICES)

    serving_size=models.CharField(max_length=200)

    created_at=models.DateTimeField(auto_now_add=True)

    owner=models.CharField(max_length=200)