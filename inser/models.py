from django.db import models
from django.utils import timezone

# Create your models here.
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
    category = models.ForeignKey(Kategorie, on_delete=models.CASCADE)
    nazwa = models.CharField(default="---", max_length=200)
    jednostka = models.CharField(max_length=200)
    cena_netto = models.PositiveIntegerField(default=0, blank=True, null=True)
    stawka_VAT = models.PositiveIntegerField(default=23, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nazwa

class Klient(models.Model):
    nabywca = models.CharField(default="---", max_length=200)
    ulica = models.CharField(default="---", max_length=200)
    miasto = models.CharField(default="---", max_length=200)
    nrTel = models.CharField(default="---", max_length=200)
    Email = models.CharField(default="---", max_length=200)
    NIP = models.CharField(default="---", max_length=200)
    rabat = models.PositiveIntegerField(default=0, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nabywca

class Pracownik(models.Model):
    sprzedawca = models.CharField(default="---", max_length=200)
    pracownik = models.CharField(default="---", max_length=200)
    ulica = models.CharField(default="---", max_length=200)
    miasto = models.CharField(default="---", max_length=200)
    nrTel = models.CharField(default="---", max_length=200)
    Email = models.CharField(default="---", max_length=200)
    NIP = models.CharField(default="---", max_length=200)
    nrKonta = models.CharField(default="---", max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.pracownik

class Faktura(models.Model):
    sprzedawca = models.ForeignKey(Pracownik, on_delete=models.CASCADE)
    nabywca = models.ForeignKey(Klient, on_delete=models.CASCADE)
    produkty = models.ManyToManyField(Usluga, related_name='faktury')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nabywca

class FakturaUsluga(models.Model):
    faktura = models.ForeignKey(Faktura, on_delete=models.CASCADE)
    usluga = models.ForeignKey(Usluga, on_delete=models.CASCADE)
    ilosc = models.PositiveIntegerField(default=1)


class Start(models.Model):
    title = models.CharField(max_length=70, blank=True, null=True)
    description = models.TextField(max_length=1024, blank=True, null=True)