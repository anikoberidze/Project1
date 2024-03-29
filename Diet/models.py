from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=100, verbose_name='საკვების დასახელება')
    category = models.CharField(max_length=100, verbose_name='კატეგორია')
    calorie = models.IntegerField(verbose_name='კალორიულობა')
    date_of_reception = models.DateField(auto_now_add=True, verbose_name='მიღების თარიღი')

    def __str__(self):
        return self.name

