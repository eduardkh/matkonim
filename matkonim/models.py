from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


# Technique
class Technique(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


# Category
class Category(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


# Difficulty
class Difficulty(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


# Ingredient
class Ingredient(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


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
    difficulty = models.ManyToManyField(Difficulty)
    image = models.ImageField(null=True, blank=True, upload_to='uploads/')
    prologue = models.TextField(null=True, blank=True)
    prep_time = models.ManyToManyField(PrepTime)
    cook_time = models.ManyToManyField(CookTime)
    ingredients = models.ManyToManyField(Ingredient)
    Instructions = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField(
        auto_now=False, auto_now_add=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
