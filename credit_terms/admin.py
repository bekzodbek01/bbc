from django.contrib import admin
from credit_terms.models import Credit_terms


@admin.register(Credit_terms)
class Credit_termsAdmin(admin.ModelAdmin):
    list_display = ('title', 'create', 'update',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_ru',  'description_uz', 'description_ru', 'file')
