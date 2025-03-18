from django.shortcuts import render
from .forms import UserForm

def user_form_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Data yang valid dapat disimpan atau digunakan sesuai kebutuhan
            return render(request, 'success.html', {'form': form})
    else:
        form = UserForm()

    return render(request, 'user_form.html', {'form': form})
