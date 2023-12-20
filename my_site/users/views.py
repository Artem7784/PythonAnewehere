from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ваш аккаунт создан: можно войти на сайт.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')


# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.views import LoginView, LogoutView
# from django.views.generic.edit import CreateView
# from django.urls import reverse_lazy
#
# class SignUpView(CreateView):
#     template_name = 'registration/signup.html'
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#
# class CustomLoginView(LoginView):
#     template_name = 'registration/login.html'
#
# class CustomLogoutView(LogoutView):
#     pass