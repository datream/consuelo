from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    context = {
        "authenticated": request.user.is_authenticated,
        "user": request.user,
    }

    return render(request, "index.html", context)
