from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.safestring import mark_safe

# Register your models here.

from .models import *



class PerimetrShopAdmin (admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'get_html_photo', 'is_published') # Список полей для админ панели в
                                                     # ЛК (изучить список атрибутов из докоментации к джанго)
    list_display_links = ('id', 'title')                                   # Ссылки на
    search_fields = ('title', 'content')                                   # Поиск по
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug', 'content', 'contents', 'param', 'photo', 'get_html_photo', 'is_published', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = 'Миниатюра'

class CategoryAdmin (admin.ModelAdmin):
    list_display = ('id', 'name', 'get_html_photo')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = 'Миниатюра'

admin.site.register(Category, CategoryAdmin)
admin.site.register(PerimetrShop, PerimetrShopAdmin)

admin.site.site_title = 'ByteBay'
admin.site.site_header = 'Управление - ByteBay'


