from django.contrib import admin
from .models import Analytics
from .models import Count
# Register your models here.

class AnalyticsAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'source','destination', )

class CountAdmin(admin.ModelAdmin):
    list_display = ('add', 'count', )

admin.site.register(Analytics, AnalyticsAdmin)
admin.site.register(Count, CountAdmin)