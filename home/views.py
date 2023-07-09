from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegistrationForm, User
from .models import Writer


# Create your views here.

class Home(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home:writers')
        else:
            return render(request, 'home/home.html')


class About(View):
    def get(self, request, username):
        return render(request, 'home/home.html')


class UserRegisterView(View):
    form_class = UserRegistrationForm
    template_name = 'home/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password1'])
            # messages.success(request, 'you registered successfully', 'success')
            return redirect('home:home')
        return render(request, self.template_name, {'form': form})


class WriterView(LoginRequiredMixin, View):
    def get(self, request):
        writers = Writer.objects.all()
        return render(request, 'home/writers.html', {'writers': writers})


