from django.contrib import admin
from . models import Todo
# Register your models here.

# admin.site.register(Todo)

@admin.register(Todo)
class Todo(admin.ModelAdmin):
    list_display = ['title','complete','pub_date']
    list_filter = ['complete', 'pub_date']
    readonly_fields = ['pub_date']
