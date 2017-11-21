from django.contrib import admin
from .models import Article,tags
# from .models import Editor

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    '''
    Customise model in admin page
    '''
    filter_horizontal = ('tags',)

# admin.site.register(Editor)
admin.site.register(Article,ArticleAdmin)
admin.site.register(tags)
