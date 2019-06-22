from django.contrib import admin
from blog.models import BlogAuthor, Blog, BlogComment

# Register your models here.
admin.site.register(BlogAuthor)
#admin.site.register(Blog)
admin.site.register(BlogComment)

class BlogCommentsInline(admin.TabularInline):
    model = BlogComment
    max_num=0

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'post_date')
    inlines = [BlogCommentsInline]
