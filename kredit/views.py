from django.shortcuts import render, redirect
from .forms import KreditForm
from .models import Kredit

def create_kredit(request):
    if request.method == 'POST':
        form = KreditForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_kredit')
    else:
        form = KreditForm()
    return render(request, 'kredit/create_kredit.html', {'form': form})

def list_kredit(request):
    kredits = Kredit.objects.all()
    return render(request, 'kredit/list_kredit.html', {'kredits': kredits})


