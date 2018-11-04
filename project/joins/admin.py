from django.contrib import admin
from .models import Join


class JoinAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'friend', 'timestamp', 'updated']
    class Meta:
        model = Join

admin.site.register(Join, JoinAdmin)
