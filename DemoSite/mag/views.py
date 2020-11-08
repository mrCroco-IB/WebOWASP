from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from .forms import NameForm
from django.http import HttpResponse

@login_required
def home(request):
    comment="<h1> My sute </h1>"
    if request.method == 'POST':
        form = NameForm(request.POST)
        comm =request.POST
        comm=dict(comm)
        comm=comm['comment']
        comment=str(comm[0])
    else:
        form = NameForm()

    return render(request, 'mag/home.html', {'form':form,'comment': comment})
def logout(request):
    return render(request, 'registration/logout.html')
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(request, user)
        return render(request, 'mag/home.html')
    else:
        form = UserCreationForm()
    return render(request, 'mag/signup.html', {'form': form})
