from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Catalog, Category


class CatalogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'code', 'vendor_code', 'brand', 'availability', 'price', 'get_photo', 'category']
    search_fields = ['title', 'vendor_code']
    list_display_links = ['id', 'title']
    list_filter = ('category',)
    list_editable = ('category',)
    actions = ['choose1']

    @admin.action(description='Изменить категорию на Ручной инструмент')
    def choose1(self, request, queryset):
        queryset.update(category=1)

    @admin.action(description='Миниатюра')
    def get_photo(self, obj):
        if obj.img_url:
            return mark_safe(f'<img src="{obj.img_url}" width="75">')
        else:
            return 'Фото не установлено'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['id', 'title']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Catalog, CatalogAdmin)


admin.site.site_title = 'Управление каталогом'
admin.site.site_header = 'Управление каталогом'
