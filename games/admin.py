
from django.contrib import admin
from .models import Category, Game

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title','category','version','updated_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title','category__name')
