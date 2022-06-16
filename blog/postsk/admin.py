from django.contrib import admin
from django.urls import clear_script_prefix

# Register your models here.
from . models import Post,Catogry,Comment

#comment inlines to link each comment to post in admin pannel
class CommentItemInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['post']

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title','intro','body']
    list_display = ['title','slug','category','created_at']
    list_filter = ['category','created_at']
    inlines = [CommentItemInline]
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']
    #auto generate slug field as per post name
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name','post','created_at']

admin.site.register(Comment,CommentAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Catogry,CategoryAdmin)