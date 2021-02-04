from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from .forms import *

# Register your models here.
class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ('email', 'is_staff', 'is_active','date_joined')
    list_filter = ('email',)
    fieldsets = (
        ('Personal Information', {
         'fields': ('email','is_staff', 'is_active','date_joined')}),
        
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active',)}
         ),
    )
    
    search_fields = ('email',)
    ordering = ('date_joined',)








admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
