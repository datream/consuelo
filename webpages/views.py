from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from webpages.forms import CustomUserCreationForm


def home_view(request, *args, **kwargs):
    context = {
        "authenticated": request.user.is_authenticated,
        "user": request.user,
    }

    return render(request, "index.html", context)


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
