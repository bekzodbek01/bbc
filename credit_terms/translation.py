from modeltranslation.translator import TranslationOptions, register
from credit_terms.models import Credit_terms


@register(Credit_terms)
class LogoTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
