from django.contrib import admin
from about.models import *
# Register your models here.


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'create', 'update', 'order',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_ru', 'description_uz', 'description_ru', 'image')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'create', 'update', 'order',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_ru', 'description_uz', 'description_ru', 'phone', 'image')


@admin.register(Connection)
class ConnectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'create', 'update', 'order',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_ru', 'description_uz', 'description_ru',)


admin.site.register(Contact)