from django.contrib import admin
from .models import Klient, Start, Usluga, Faktura, Pracownik, Kategorie, FakturaUsluga

admin.site.register(Start)
admin.site.register(Klient)
admin.site.register(Pracownik)

class UslugaInline(admin.TabularInline):
    model = Usluga

@admin.register(Kategorie)
class KategoriaAdmin(admin.ModelAdmin):
    inlines = [UslugaInline]

class FakturaUslugaInline(admin.TabularInline):
    model = FakturaUsluga
    extra = 1

@admin.register(Faktura)
class FakturaAdmin(admin.ModelAdmin):
    inlines = [FakturaUslugaInline]
    list_filter = ('produkty__category',)

@admin.register(Usluga)
class UslugaAdmin(admin.ModelAdmin):
    list_filter = ('category',)
