from django.shortcuts import render
from .forms import ApplicationForm
# Create your views here.


def application_view(request):
    form = ApplicationForm
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form_data': form
    }
    return render(request, 'app.html', context)
