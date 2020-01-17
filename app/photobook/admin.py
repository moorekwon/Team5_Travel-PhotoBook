from django.contrib import admin

from photobook.models import PhotoBook, Page, Photo


@admin.register(PhotoBook)
class PhotoBookAdmin(admin.ModelAdmin):
    pass


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    pass


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
