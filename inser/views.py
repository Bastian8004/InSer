from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from django.urls import reverse
from django.forms import formset_factory
from .forms import KategoriaForm, KlientForm, PracownikForm, UslugaForm, FakturaForm
from .models import Klient, Kategorie, Pracownik, Usluga, Faktura, Start
from django.http import HttpResponseRedirect
from django.http import JsonResponse

# Widok startowy
def start(request):
    starts = Start.objects.all().order_by()
    return render(request, 'start.html', {'starts': starts})

# Widok kategorii
def kategoria(request):
    kategories = Kategorie.objects.all().order_by('-published_date')
    return render(request, 'kategorie.html', {'kategories': kategories})

# Widok usług w kategorii
def uslugi(request, pk):
    kategoria = get_object_or_404(Kategorie, pk=pk)
    uslugas = Usluga.objects.filter(category=kategoria)
    return render(request, 'uslugi.html', {'kategoria': kategoria, 'uslugas': uslugas})

# Widok tworzenia nowej kategorii
def kategoria_new(request):
    if request.method == "POST":
        form = KategoriaForm(request.POST, request.FILES)
        if form.is_valid():
            kategoria = form.save(commit=False)
            kategoria.published_date = timezone.now()
            kategoria.save()
            return redirect('kategorie')
    else:
        form = KategoriaForm()
    return render(request, 'Kategoria/kategoria_new.html', {'form': form})

# Widok edycji kategorii
def kategoria_edit(request, pk):
    kategoria = get_object_or_404(Kategorie, pk=pk)
    if request.method == "POST":
        form = KategoriaForm(request.POST, request.FILES, instance=kategoria)
        if form.is_valid():
            kategoria = form.save(commit=False)
            kategoria.published_date = timezone.now()
            kategoria.save()
            return redirect('kategorie')
    else:
        form = KategoriaForm(instance=kategoria)
    return render(request, 'Kategoria/kategoria_edit.html', {'form': form, 'kategoria': kategoria})

def kategoria_delete(request, pk):
    kategoria = get_object_or_404(Kategorie, pk=pk)
    kategoria.delete()
    return redirect(reverse('kategorie'))

# Widok tworzenia nowej usługi
def usluga_new(request):
    if request.method == "POST":
        form = UslugaForm(request.POST, request.FILES)
        if form.is_valid():
            usluga = form.save(commit=False)
            usluga.published_date = timezone.now()
            usluga.save()
            return redirect('uslugi', pk=usluga.pk)
    else:
        form = UslugaForm()
    return render(request, 'Usluga/usluga_new.html', {'form': form})

# Widok edycji usługi
def usluga_edit(request, pk):
    usluga = get_object_or_404(Usluga, pk=pk)
    if request.method == "POST":
        form = UslugaForm(request.POST, request.FILES, instance=usluga)
        if form.is_valid():
            usluga = form.save(commit=False)
            usluga.published_date = timezone.now()
            usluga.save()
            return redirect('uslugi', pk=usluga.category.pk)
    else:
        form = UslugaForm(instance=usluga)
    return render(request, 'Usluga/usluga_edit.html', {'form': form, 'usluga': usluga})

def usluga_delete(request, pk):
    usluga = get_object_or_404(Usluga, pk=pk)
    usluga.delete()
    return redirect('uslugi', pk=usluga.category.pk)

# Widok klientów
def klient(request):
    klients = Klient.objects.all().order_by('-published_date')
    return render(request, 'klient.html', {'klients': klients})

# Szczegóły klienta
def klient_detail(request, pk):
    klient = get_object_or_404(Klient, pk=pk)
    return render(request, 'Klient/klient_detail.html', {'klient': klient})

# Widok tworzenia nowego klienta
def klient_new(request):
    if request.method == "POST":
        form = KlientForm(request.POST, request.FILES)
        if form.is_valid():
            klient = form.save(commit=False)
            klient.published_date = timezone.now()
            klient.save()
            return redirect('klient_detail', pk=klient.pk)
    else:
        form = KlientForm()
    return render(request, 'Klient/klient_new.html', {'form': form})

# Widok edycji klienta
def klient_edit(request, pk):
    klient = get_object_or_404(Klient, pk=pk)
    if request.method == "POST":
        form = KlientForm(request.POST, request.FILES, instance=klient)
        if form.is_valid():
            klient = form.save(commit=False)
            klient.published_date = timezone.now()
            klient.save()
            return redirect('klient_detail', pk=klient.pk)
    else:
        form = KlientForm(instance=klient)
    return render(request, 'Klient/klient_edit.html', {'form': form})

def klient_delete(request, pk):
    klient = get_object_or_404(Klient, pk=pk)
    klient.delete()
    return redirect(reverse('klient'))

# Widok sprzedawców
def sprzedawca(request):
    sprzedawcas = Pracownik.objects.all().order_by('-published_date')
    return render(request, 'sprzedawca.html', {'sprzedawcas': sprzedawcas})

# Szczegóły sprzedawcy
def sprzedawca_detail(request, pk):
    sprzedawca = get_object_or_404(Pracownik, pk=pk)
    return render(request, 'Sprzedawca/sprzedawca_detail.html', {'sprzedawca': sprzedawca})

# Widok tworzenia nowego sprzedawcy
def sprzedawca_new(request):
    if request.method == "POST":
        form = PracownikForm(request.POST, request.FILES)
        if form.is_valid():
            sprzedawca = form.save(commit=False)
            sprzedawca.published_date = timezone.now()
            sprzedawca.save()
            return redirect('sprzedawca_detail', pk=sprzedawca.pk)
    else:
        form = PracownikForm()
    return render(request, 'Sprzedawca/sprzedawca_new.html', {'form': form})

# Widok edycji sprzedawcy
def sprzedawca_edit(request, pk):
    sprzedawca = get_object_or_404(Pracownik, pk=pk)
    if request.method == "POST":
        form = PracownikForm(request.POST, request.FILES, instance=sprzedawca)
        if form.is_valid():
            sprzedawca = form.save(commit=False)
            sprzedawca.published_date = timezone.now()
            sprzedawca.save()
            return redirect('sprzedawca_detail', pk=sprzedawca.pk)
    else:
        form = PracownikForm(instance=sprzedawca)
    return render(request, 'Sprzedawca/sprzedawca_edit.html', {'form': form})

def sprzedawca_delete(request, pk):
    sprzedawca = get_object_or_404(Pracownik, pk=pk)
    sprzedawca.delete()
    return redirect(reverse('sprzedawca'))

# Widok faktur
def faktura(request):
    fakturas = Faktura.objects.all().order_by('-published_date')
    return render(request, 'faktura.html', {'fakturas': fakturas})

# Szczegóły faktury
def faktura_detail(request, pk):
    faktura = get_object_or_404(Faktura, pk=pk)
    return render(request, 'Faktura/faktura_detail.html', {'faktura': faktura})

# Widok tworzenia nowej faktury
def faktura_new(request):
    if request.method == "POST":
        form = FakturaForm(request.POST, request.FILES)
        if form.is_valid():
            faktura = form.save(commit=False)
            faktura.published_date = timezone.now()
            faktura.save()
            return redirect('faktura_detail', pk=faktura.pk)
    else:
        form = FakturaForm()
    return render(request, 'Faktura/faktura_new.html', {'form': form})

# Widok edycji faktury
def faktura_edit(request, pk):
    faktura = get_object_or_404(Faktura, pk=pk)
    if request.method == "POST":
        form = FakturaForm(request.POST, request.FILES, instance=faktura)
        if form.is_valid():
            faktura = form.save(commit=False)
            faktura.published_date = timezone.now()
            faktura.save()
            return redirect('faktura_detail', pk=faktura.pk)
    else:
        form = FakturaForm(instance=faktura)
    return render(request, 'Faktura/faktura_edit.html', {'form': form})

def load_uslugi(request, category_id):
    uslugi = Usluga.objects.filter(category_id=category_id)
    options = list(uslugi.values('id', 'nazwa'))
    return JsonResponse(options, safe=False)

def fakrura_delete(request, pk):
    faktura = get_object_or_404(Faktura, pk=pk)
    faktura.delete()
    return redirect(reverse('faktura'))

