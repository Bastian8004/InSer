from django.db import models
from django.utils import timezone

# Create your models here.

class Start(models.Model):
    title = models.CharField(max_length=70, blank=True, null=True)
    description = models.TextField(max_length=1024, blank=True, null=True)

class Kategorie(models.Model):
    nazwa = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nazwa

class Usluga(models.Model):
    category = models.ForeignKey(Kategorie, on_delete=models.CASCADE, related_name='uslugi')
    nazwa = models.CharField(max_length=200)
    jednostka = models.CharField(max_length=200)
    cena_netto = models.PositiveIntegerField(default=0, blank=True, null=True)
    stawka_VAT = models.PositiveIntegerField(default=23, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    @property
    def cena_brutto(self):
        return self.cena_netto * (1 + self.stawka_VAT / 100)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nazwa

class Klient(models.Model):
    nabywca = models.CharField(max_length=200)
    ulica = models.CharField(max_length=200)
    miasto = models.CharField(max_length=200)
    nrTel = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    NIP = models.CharField(max_length=200)
    rabat = models.PositiveIntegerField(default=0, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nabywca

class Pracownik(models.Model):
    sprzedawca = models.CharField(max_length=200)
    pracownik = models.CharField(max_length=200)
    ulica = models.CharField(max_length=200)
    miasto = models.CharField(max_length=200)
    nrTel = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    NIP = models.CharField(max_length=200)
    nrKonta = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.pracownik

class Faktura(models.Model):
    sprzedawca = models.ForeignKey(Pracownik, on_delete=models.CASCADE)
    nabywca = models.ForeignKey(Klient, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Faktura {self.id} - {self.nabywca}"

    @property
    def suma_netto(self):
        return sum(pozycja.cena_netto for pozycja in self.pozycje.all())

    @property
    def suma_brutto(self):
        return sum(pozycja.cena_brutto for pozycja in self.pozycje.all())

class FakturaUsluga(models.Model):
    faktura = models.ForeignKey(Faktura, on_delete=models.CASCADE, related_name='pozycje')
    category = models.ForeignKey(Kategorie, on_delete=models.CASCADE, related_name='faktura_uslugi')
    uslugi = models.ForeignKey(Usluga, on_delete=models.CASCADE, related_name='faktura_uslugi')
    ilosc = models.PositiveIntegerField(default=1)

    @property
    def cena_netto(self):
        return self.uslugi.cena_netto * self.ilosc

    @property
    def cena_brutto(self):
        return self.uslugi.cena_brutto * self.ilosc

    def __str__(self):
        return f"Pozycja na fakturze {self.faktura_id}: {self.uslugi.nazwa}"