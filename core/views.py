from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from item.models import Category, Item
from .forms import SignupForm, LoginForm
from django.contrib import messages
from django.contrib.auth.views import LoginView

def home(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Verify reCAPTCHA
            captcha_value = request.POST.get('g-recaptcha-response', '')
            if not captcha_value or not form.fields['captcha'].verify(captcha_value, request.META.get('REMOTE_ADDR')):
                messages.error(request, "Error verifying reCAPTCHA, please try again.")
            else:
                # reCAPTCHA verification successful
                messages.success(request, "Success!")
        else:
            messages.error(request, "Form validation error!")
    else:
        form = LoginForm()
    
    return render(request, 'index.html', {'form': form})

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "index.html" 

class CustomLoginView(LoginView):
    template_name = 'core/index.html'
    authentication_form = LoginForm

    def form_valid(self, form):
        # Verify reCAPTCHA
        captcha_value = self.request.POST.get('g-recaptcha-response', '')
        if not captcha_value or not form.fields['captcha'].verify(captcha_value, self.request.META.get('REMOTE_ADDR')):
            messages.error(self.request, "Error verifying reCAPTCHA, please try again.")
            return self.form_invalid(form)

        # reCAPTCHA verification successful
        messages.success(self.request, "Success!")
        return super().form_valid(form)