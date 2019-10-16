from django.contrib import admin
from .models import *

class MatkonModelAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'updated', 'timestamp']
    list_display_links = ['updated']
    list_filter = ['updated', 'timestamp']

    class Meta:
        model = Matkon


admin.site.register(Matkon, MatkonModelAdmin)
admin.site.register(Ingredient)
admin.site.register(Technique)
admin.site.register(Category)
admin.site.register(PrepTime)
admin.site.register(CookTime)
admin.site.register(Difficulty)
admin.site.register(Quantity)
