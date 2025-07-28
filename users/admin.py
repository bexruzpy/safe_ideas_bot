from django.contrib import admin
from .models import User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'end_use_date', 'is_active')
    search_fields = ('tg_id', 'first_name', 'last_name')
    list_filter = ('is_active', 'created_at')
    ordering = ('-created_at',)
    
    def full_name(self, obj):
        return obj.full_name()
    
    def end_use(self, obj):
        return obj.end_use_date.strftime('%H:%M | %d - %B %Y') if obj.end_use_date else 'N/A'
    end_use.short_description = 'End Use Date'

    full_name.short_description = 'Full Name'
