from django.contrib import admin

import src.core.models as models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display_links = ('name', 'id',)
    list_display = ('name', 'created_at', 'updated_at', 'id')

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display_links = ('name', 'id',)
    list_display = ('name', 'created_at', 'updated_at', 'id', 'author', 'published_date', 'book_images', 'category',)
    list_filter = ('category', 'updated_at')

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    ...

@admin.register(models.Rating)
class RatingAdmin(admin.ModelAdmin):
    ...


