from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CreativeUser, Post, Comment


class CreativeUserAdmin(UserAdmin):
    list_display = (
        'full_name',
        'email',
        'location',
        'is_active',
        'is_staff',
        'is_superuser',
    )

    list_editable = ("is_active",)

    ordering = ('full_name',)
    search_fields = ('full_name', 'email', 'location')
    readonly_fields = ('password', 'date_joined', 'last_login')

    fieldsets = (
        ('User Login fields', {"fields": ('email', 'full_name',)}),
        ('Personal Details', {"fields": ('profile_pic', 'location', 'bio')}),
        ('Social links', {"fields": ('facebook', 'instagram', 'twitter', 'linkedin')}),
        ('Social fields', {"fields": ('follows',)}),
    )

    add_fieldsets = (
        (None, ({"fields": ("email", "full_name", "password1", "password2")})),
    )

    filter_horizontal = ()
    list_filter = ()


admin.site.register(CreativeUser, CreativeUserAdmin)

admin.site.register(Post)
admin.site.register(Comment)
