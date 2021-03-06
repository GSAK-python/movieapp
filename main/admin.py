from django.contrib import admin
from .models import Movie, ExtraInfo, Review, Aktor

# Register your models here.


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ('name', 'description', 'year')  $ tylko te sie wyswietlaja
    list_display = ('name', 'description', 'year', 'released')
    list_filter = ('year', 'released')
    search_fields = ('year', 'description')

admin.site.register(ExtraInfo)
admin.site.register(Review)
admin.site.register(Aktor)