from django.contrib import admin
from .models import Klient, Start, Usluga, Faktura, Pracownik, Kategorie, FakturaUsluga
from .forms import FakturaUslugaForm

admin.site.register(Start)
admin.site.register(Klient)
admin.site.register(Pracownik)

class UslugaInline(admin.TabularInline):
    model = Usluga

@admin.register(Kategorie)
class KategoriaAdmin(admin.ModelAdmin):
    inlines = [UslugaInline]
    extra = 1

class FakturaUslugaInline(admin.TabularInline):
    model = FakturaUsluga
    form = FakturaUslugaForm
    extra = 1

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "uslugi":
            try:
                category_id = request.POST.get('category')
                if category_id:
                    kwargs['queryset'] = Usluga.objects.filter(category_id=category_id)
                else:
                    kwargs['queryset'] = Usluga.objects.none()
            except ValueError:
                kwargs['queryset'] = Usluga.objects.none()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class FakturaAdmin(admin.ModelAdmin):
    inlines = [FakturaUslugaInline]

admin.site.register(Faktura, FakturaAdmin)
