from django.contrib import admin
from .models import Matkon

class MatkonModelAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'sections', 'updated']
    list_display_links = ['updated']
    list_filter = ['updated', 'timestamp']

    class Meta:
        model = Matkon


admin.site.register(Matkon, MatkonModelAdmin)
