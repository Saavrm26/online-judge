""" Django admin customization """

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models
from problem import models as problem_model


class UserAdmin(BaseUserAdmin):
    """ Define the admin pages for users """
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (
            None,
            {'fields': ('email', 'password')}
        ),
        (
            _('Permission'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (
            _('Important Dates'),
            {
                'fields': ('last_login',)
            }
        )
    )
    readonly_fields = ['last_login']

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'password1',
                    'password2',
                    'name',
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
    )


class TPjoin_inline(admin.TabularInline):
    ordering = ['tag']
    model = problem_model.TPjoin
    extra = 1


class ProblemAdmin(admin.ModelAdmin):
    """ Defines the Problem page for admin """
    ordering = ['id']
    list_display = ['id', 'name', 'difficulty']
    inlines = [TPjoin_inline]
    filter_horizontal = ['tags']


class TagAdmin(admin.ModelAdmin):
    """ Define the Tags page for admin """
    list_display = ['name']
    ordering = ['name']


admin.site.register(models.User, UserAdmin)
admin.site.register(problem_model.Problem, ProblemAdmin)
admin.site.register(problem_model.Tag, TagAdmin)
