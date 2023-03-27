from django.contrib import admin


from .models import (
    Question, Choice
)

# admin.site.register(Question)
admin.site.register(Choice)

class ProductChoiceInline(admin.TabularInline):
    model = Choice
    readonly_fields = ('id',)
    extra = 1
    classes = ('collapse', )
    show_change_link = True
    def has_add_permission(self, request, obj):
        return True
    def has_delete_permission(self, request, obj=None):
        return True
    def has_change_permission(self, request, obj=None):
        return True


@admin.register(Question)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductChoiceInline]