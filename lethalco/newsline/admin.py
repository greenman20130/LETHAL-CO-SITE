from django.contrib import admin
from .models import Post, Message
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
 
# создаём новый класс для представления товаров в админке
class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(), label="Контент")
    list_display =  ('title', 'text', 'user_id')
    list_filter = ('user_id', 'pclass',)
    search_fields = ('title',)
    class Meta:
        model = Post
        fields = '__all__'
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm 
# Register your models here.
 
admin.site.register(Post, PostAdmin)
admin.site.register(Message)