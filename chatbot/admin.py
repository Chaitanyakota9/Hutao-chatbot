from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.db.models import Avg
from .models import Chat

# Custom admin site header and title
admin.site.site_header = "Hu Tao's Parlor Admin 💀"
admin.site.site_title = "Hu Tao Admin"
admin.site.index_title = "Welcome to the Wangsheng Funeral Parlor Management System"

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('user', 'message_preview', 'response_preview', 'created_at', 'message_length')
    list_filter = ('created_at', 'user')
    search_fields = ('user__username', 'message', 'response')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    list_per_page = 25
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Chat Information', {
            'fields': ('user', 'created_at')
        }),
        ('Message Content', {
            'fields': ('message', 'response'),
            'classes': ('wide',)
        }),
    )
    
    def message_preview(self, obj):
        """Show first 50 characters of message"""
        return obj.message[:50] + '...' if len(obj.message) > 50 else obj.message
    message_preview.short_description = 'Message'
    
    def response_preview(self, obj):
        """Show first 50 characters of response"""
        return obj.response[:50] + '...' if len(obj.response) > 50 else obj.response
    response_preview.short_description = 'Hu Tao\'s Response'
    
    def message_length(self, obj):
        """Show message length"""
        return f"{len(obj.message)} chars"
    message_length.short_description = 'Length'
    
    # Admin actions
    actions = ['delete_old_chats', 'view_chat_stats']
    
    # Custom admin styling
    class Media:
        css = {
            'all': ('admin/css/hutao_admin.css',)
        }

# Customize User admin
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'date_joined')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('-date_joined',)
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

# Unregister the default User admin and register our custom one
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Add some helpful admin actions
@admin.action(description="Delete old chats (older than 30 days)")
def delete_old_chats(modeladmin, request, queryset):
    from django.utils import timezone
    from datetime import timedelta
    
    cutoff_date = timezone.now() - timedelta(days=30)
    old_chats = queryset.filter(created_at__lt=cutoff_date)
    count = old_chats.count()
    old_chats.delete()
    
    from django.contrib import messages
    messages.success(request, f"Deleted {count} old chat records.")

@admin.action(description="View chat statistics")
def view_chat_stats(modeladmin, request, queryset):
    from django.contrib import messages
    
    total_chats = queryset.count()
    unique_users = queryset.values('user').distinct().count()
    
    messages.info(request, f"Stats: {total_chats} total chats, {unique_users} unique users")


