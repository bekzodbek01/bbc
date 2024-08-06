from django.contrib import admin
from car.models import *


@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ('title', 'create', 'update', 'order',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_ru',  'description_uz', 'description_ru', 'image')


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('title', 'create', 'update', 'order',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_ru',  'description_uz', 'description_ru', 'filed_km', 'year', 'price', 'logo', 'image',
              'color')


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'create', 'update', 'order',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_ru',  'description_uz', 'description_ru', 'image')


class Contractsub(admin.TabularInline):
    model = Contractsub
    fields = ['inital_payment', 'month', 'year',]


@admin.register(Contract)
class Contract(admin.ModelAdmin):
    list_display =('create', 'update')
    inlines = [Contractsub]
    fields = ('car',)


