from django import forms
from inser.models import Kategorie, Usluga, Faktura, Klient, Pracownik, FakturaUsluga

class KategoriaForm(forms.ModelForm):

    class Meta:
        model = Kategorie
        fields = ['nazwa', 'created_date', 'published_date']

class UslugaForm(forms.ModelForm):

    class Meta:
        model = Usluga
        fields = ['nazwa','jednostka','cena_netto','stawka_VAT', 'created_date', 'published_date']

class FakturaForm(forms.ModelForm):
    produkty = forms.ModelMultipleChoiceField(
        queryset=Usluga.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = Faktura
        fields = ['sprzedawca', 'nabywca', 'produkty', 'created_date', 'published_date']

class FakturaUslugaForm(forms.ModelForm):
    class Meta:
        model = FakturaUsluga
        fields = ['faktura', 'usluga', 'ilosc']

class KlientForm(forms.ModelForm):

    class Meta:
        model = Klient
        fields = ['nabywca','ulica','miasto','nrTel','Email','NIP','rabat', 'created_date', 'published_date']

class PracownikForm(forms.ModelForm):

    class Meta:
        model = Pracownik
        fields = ['sprzedawca','pracownik', 'ulica','miasto','nrTel','Email','NIP','nrKonta', 'created_date', 'published_date']