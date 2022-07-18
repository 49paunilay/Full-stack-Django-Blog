from django.contrib import admin
from .models import Category, Comments,Post,ContactUser,AdminTasks
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','description','add_date')
    search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','cat')
    search_fields = ('title','content')

    class Media:
        js=('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js','js/script.js')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'body', 'post', 'created_date', 'active')
    list_filter = ('active', 'created_date')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self,request,queryset):
        queryset.update(active=True)

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(ContactUser)
admin.site.register(Comments,CommentAdmin)
admin.site.register(AdminTasks)

