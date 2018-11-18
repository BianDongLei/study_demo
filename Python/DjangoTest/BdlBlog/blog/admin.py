from django.contrib import admin

# Register your models here.

from . import models

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "create_time", "update_time")
    list_filter = ("create_time",)
admin.site.register(models.Article, ArticleAdmin)