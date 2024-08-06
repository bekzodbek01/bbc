from modeltranslation.translator import TranslationOptions, register
from about.models import About, News, Contact, Connection


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Connection)
class ConnectionTranslationOptions(TranslationOptions):
    fields = ('title',)
