from django.contrib import admin
from .models import Category, Author, New, AdditionalImg

# Register your models here.

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(New)
admin.site.register(AdditionalImg)

