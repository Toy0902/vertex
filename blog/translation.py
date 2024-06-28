from modeltranslation.translator import register, TranslationOptions, translator
from blog.models import Matn, Rasmlar
@register(Matn)
class NewsTranslationOp(TranslationOptions):
    fields = ('nomi', 'text', 'chopetilish_vaqti')

@register(Rasmlar)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('nomi',)


