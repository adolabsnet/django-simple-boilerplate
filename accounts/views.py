from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse

from .forms import ProfileForm, UserForm
from .models import Profile

def RegisterView(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            user = authenticate(username=user_form.cleaned_data['username'],
                                password=user_form.cleaned_data['password'])
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
            login(request,user)
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request,'accounts/register.html',
                          {
                              'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})


def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponse("Invalid login details")
    else:
        return render(request, 'accounts/login.html', {})


@login_required
def LogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def DashboardView(request):
    response = request.user
    profile = Profile.objects.filter(user=response)

    return render(request, 'accounts/dashboard.html', {'profile':profile})
