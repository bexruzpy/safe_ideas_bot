from django.contrib import admin
from .models import Project, Function, ComfortTime, Plan
# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at', 'updated_at', 'is_active')
    search_fields = ('title', 'user__first_name', 'user__last_name')
    list_filter = ('is_active', 'created_at')
    ordering = ('-created_at',)
@admin.register(Function)
class FunctionAdmin(admin.ModelAdmin):
    list_display = ('view_titile', 'project', 'type', 'file_id', 'created_at')
    search_fields = ('text', 'project__title')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    def view_titile(self, obj):
        if obj.text:
            return obj.text
        return obj.type
    view_titile.short_description = 'Title'
@admin.register(ComfortTime)
class ComfortTimeAdmin(admin.ModelAdmin):
    list_display = ('user', 'time')
    search_fields = ('user__first_name', 'user__last_name')
    list_filter = ('time',)
    ordering = ('-time',)
