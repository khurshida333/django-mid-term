from django.shortcuts import render,redirect
from .import forms
from cars.models import Car
from django.contrib.auth.forms import AuthenticationForm ,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required




# Create your views here.

def register(request):
    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account created successfully !!')
            return redirect('Login')
        else:
            return render(request, 'register.html', {'form': register_form, 'type': 'Register'})
    else:
        register_form = forms.RegisterForm()
        return render(request, 'register.html',{'form': register_form, 'type':'Register'})

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class UserLogInView(LoginView):
    template_name = 'register.html'
    # success_url = reverse_lazy('Profile') #redirect
    def get_success_url(self):
        return reverse_lazy('Profile')
    
    def form_valid(self, form):
        messages.success(self.request, 'logged in successfully !')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'logged in information incorrect (X)')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["type"] = 'Login'
            return context

def user_logout(request):
    logout(request)
    return  redirect('Login')

@login_required
def profile(request):
    if request.user.is_authenticated:
       user = request.user
       purchased_cars = user.purchased_cars.all()  # Get cars purchased by the user
       return render(request, 'profile.html', {'purchased_cars': purchased_cars})
    else:
        return redirect('Login')

@login_required
def edit_profile(request):
    if request.user.is_authenticated:
      if request.method == 'POST':
          profile_form = forms.ChangeUserData(request.POST, instance=request.user)
          if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile UPDATED successfully !!')
            return redirect('Edit_profile')
          else:
            return render(request, 'update_profile.html', {'form': profile_form})
      else:
        profile_form = forms.ChangeUserData(instance=request.user)
        return render(request, 'update_profile.html',{'form': profile_form})
    else:
        return redirect('Login')

def change_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
               form.save()
               update_session_auth_hash(request, form.user) #it ensures the user remains logged in
               messages.success(request, 'Password UPDATED successfully !!')
               return redirect('Profile')
            else:
               return render(request, 'change_pass.html', {'form': form})
        else:
           form = PasswordChangeForm(user=request.user)
           return render(request, 'change_pass.html',{'form': form})
    else:
        return redirect('Login')