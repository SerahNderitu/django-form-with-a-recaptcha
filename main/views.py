
from django.shortcuts import render, HttpResponse
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            return HttpResponse("You're human.You can proceed now.")
        else:
            return HttpResponse("Something is wrong! Bot detected.")

    else:
        form = ContactForm
    return render(request, 'contact.html', {'form': form})
