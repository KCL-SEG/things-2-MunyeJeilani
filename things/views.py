from django.shortcuts import render
from .forms import ThingForm

def home(request):
    if request.method == 'POST':
        form = ThingForm(request.POST)
        if form.is_valid():
            # Process the form data if it's valid
            # For example, you can save it to the database
            form.save()
    else:
        form = ThingForm()

    return render(request, 'home.html', {'form': form})
