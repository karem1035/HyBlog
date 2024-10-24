from django.contrib import admin
from .models import Post, Category, Section
from django.utils.html import format_html


class SectionInline(admin.TabularInline):
    model = Section
    extra = 1  # Allows adding one extra section by default


class PostAdmin(admin.ModelAdmin):
    inlines = [SectionInline]
    list_display = ('title', 'category', 'created_at', 'image_tag')
    fields = ['title', 'content', 'category', 'image', 'created_at']

    readonly_fields = ('created_at', 'image_tag')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width: 200px;"/>'.format(obj.image.url))
        return "No Image"
    image_tag.short_description = 'Image Preview'


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Section)
