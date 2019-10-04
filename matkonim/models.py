from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Matkon(models.Model):
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, default=1, null=True,
                               on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    sections = models.CharField(max_length=120)
    image = models.ImageField(null=True, blank=True, upload_to='uploads/')
    prologue = models.TextField(null=True, blank=True)
    prep_time = models.CharField(max_length=120, null=True, blank=True)
    cook_time = models.CharField(max_length=120, null=True, blank=True)
    ingredients = models.TextField(null=True, blank=True)
    Instructions = models.TextField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField(
        auto_now=False, auto_now_add=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
