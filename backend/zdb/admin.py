from django.contrib import admin
from .models import Tag, Movie
# Register your models here.
class TagAdmin(admin.ModelAdmin):
    pass

class MovieAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tag, TagAdmin)
admin.site.register(Movie, MovieAdmin)