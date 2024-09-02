from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

class BlogsAdmin(SummernoteModelAdmin):
    search_fields = ['title', 'keywords']
    list_filter = ['status', 'categories']
    readonly_fields = ['thumb_image', 'viewCount', 'shareCount', 'dateAdded', 'lastUpdated']
    save_as = True
    summernote_fields = ('content',)

    def thumb_image(self, obj):
        return mark_safe(
            
            f'<img src="{obj.image.url}" id="blogImg" width="250" height="250" />'+
            """
            <script>
            id_image.onchange = evt => {
            const [file] = id_image.files
            if (file) {
                blogImg.src = URL.createObjectURL(file)
            }
            }
            </script>
            """
        )

admin.site.register(Blogs, BlogsAdmin)

admin.site.register(BlogCategorie)
admin.site.register(BlogKeyword)