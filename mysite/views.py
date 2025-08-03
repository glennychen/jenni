from django.shortcuts import render, redirect
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

def home(request):
    return render(request, 'homepage.html', {})

def about(request):
    return render(request, 'about.html', {})

def faq(request):
    return render(request, 'faq.html', {})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # TODO: Manually save data to the database
            return redirect('success')  # Redirect after successful submission
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def project(request):
    return render(request, 'project.html', {})