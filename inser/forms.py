from django import forms
from .models import Kategorie, Usluga, Faktura, Klient, Pracownik, FakturaUsluga

class FakturaUslugaForm(forms.ModelForm):
    class Meta:
        model = FakturaUsluga
        fields = ['faktura', 'category', 'uslugi', 'ilosc']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['uslugi'].queryset = Usluga.objects.none()  # Rozpoczynamy z pustym zbiorem opcji

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['uslugi'].queryset = Usluga.objects.filter(category_id=category_id).order_by('nazwa')
            except (ValueError, TypeError):
                pass  # W przypadku problemu, zachowujemy puste pole wyboru
        elif self.instance.pk:
            self.fields['uslugi'].queryset = self.instance.category.uslugi.order_by('nazwa')

class KategoriaForm(forms.ModelForm):
    class Meta:
        model = Kategorie
        fields = ['nazwa', 'created_date', 'published_date']

class UslugaForm(forms.ModelForm):
    class Meta:
        model = Usluga
        fields = ['nazwa', 'jednostka', 'cena_netto', 'stawka_VAT', 'category', 'created_date', 'published_date']

class FakturaForm(forms.ModelForm):
    produkty = forms.ModelMultipleChoiceField(
        queryset=Usluga.objects.all()
    )
    class Meta:
        model = Faktura
        fields = ['sprzedawca', 'nabywca', 'created_date', 'published_date']

class KlientForm(forms.ModelForm):
    class Meta:
        model = Klient
        fields = ['nabywca', 'ulica', 'miasto', 'nrTel', 'Email', 'NIP', 'rabat', 'created_date', 'published_date']

class PracownikForm(forms.ModelForm):
    class Meta:
        model = Pracownik
        fields = ['sprzedawca', 'pracownik', 'ulica', 'miasto', 'nrTel', 'Email', 'NIP', 'nrKonta', 'created_date', 'published_date']
