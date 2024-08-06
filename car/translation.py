from modeltranslation.translator import TranslationOptions, register
from car.models import Logo, Slider, Car


@register(Logo)
class LogoTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(Car)
class CarTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(Slider)
class SliderTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)






