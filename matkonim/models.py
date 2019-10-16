from django.db import models
from django.conf import settings
from datetime import datetime

User = settings.AUTH_USER_MODEL


# Technique
class Technique(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


# Category
class Category(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


# Difficulty - Choices
class Difficulty(models.Model):
    option = models.CharField(max_length=120)

    def __str__(self):
        return self.option


# Ingredient
class Ingredient(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


# Prep Time
class PrepTime(models.Model):
    prep_time = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.prep_time)


# Cook Time
class CookTime(models.Model):
    cook_time = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.cook_time)


class Matkon(models.Model):
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, default=1, null=True,
                               on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    category = models.ManyToManyField(Category)
    techniques = models.ManyToManyField(Technique)
    difficulty = models.ForeignKey(
        Difficulty, default=1, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='uploads/')
    prologue = models.TextField(null=True, blank=True)
    prep_time = models.ForeignKey(
        PrepTime, default=1, on_delete=models.SET_NULL, null=True, blank=True)
    cook_time = models.ForeignKey(
        CookTime, default=1, on_delete=models.SET_NULL, null=True, blank=True)
    ingredients = models.ManyToManyField(Ingredient, through='Quantity')
    Instructions = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField(
        auto_now=False, auto_now_add=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=False, default=datetime.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# quantity
class Quantity(models.Model):
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.SET_NULL, null=True, blank=True)
    matkon = models.ForeignKey(
        Matkon, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return 'Quantity:{} Ingredient:{} Matkon:{}'.format(str(self.quantity), str(self.ingredient), str(self.matkon))
