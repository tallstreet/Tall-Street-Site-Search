from django.contrib import admin
from search.models import Page
from settings import MEDIA_URL

class PageAdmin(admin.ModelAdmin):
    list_display = ('url',)
    exclude = ('update_time', 'create_time', 'change_time',)

admin.site.register(Page, PageAdmin)
