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
    list_display = ('email','full_name','current_balance','is_staff', 'is_active')
    list_filter = ('email',)
    fieldsets = (
        ('Personal Information', {
         'fields': ('email','full_name','current_balance','is_staff', 'is_active',)}),
        
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','password1','password2','full_name','current_balance', 'is_staff', 'is_active',)}
         ),
    )
    
    search_fields = ('email',)
    ordering = ('date_joined',)

class  TransactionAdmin(admin.ModelAdmin):
    list_display = ('sender','recipient','amount','created_at','status')



admin.site.register(Transaction, TransactionAdmin)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
