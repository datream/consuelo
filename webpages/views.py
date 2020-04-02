from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from webpages.forms import CustomUserCreationForm, CustomUserUpdationForm


def home_view(request, *args, **kwargs):
    context = {
        "authenticated": request.user.is_authenticated,
        "user": request.user,
    }

    return render(request, "index.html", context)


def about_view(request, *args, **kwargs):
    context = {
        "authenticated": request.user.is_authenticated,
        "user": request.user,
    }

    return render(request, "about.html", context)


def services_view(request, *args, **kwargs):
    context = {
        "authenticated": request.user.is_authenticated,
        "user": request.user,
    }

    return render(request, "services.html", context)


def contact_view(request, *args, **kwargs):
    context = {
        "authenticated": request.user.is_authenticated,
        "user": request.user,
    }

    return render(request, "contact.html", context)


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account created successfully')
                return redirect('home')

        else:
            form = CustomUserCreationForm()

        return render(request, 'registration/signup.html', {'form': form})


def settings_view(request):
    if request.user.is_anonymous:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = CustomUserUpdationForm(request.POST)
            if form.is_valid():
                form.save(request.user)

        else:
            form = CustomUserUpdationForm()

        return render(request, 'registration/settings.html', {'form': form})
