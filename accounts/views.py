from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from actions.models import Action
from rewards.models import Reward
from histories.models import History

@login_required
def mypage(request):
    actions = Action.objects.filter(user=request.user)
    rewards = Reward.objects.filter(user=request.user)
    histories = History.objects.filter(user=request.user).order_by('-created_at')
    points = request.user.point 
    return render(request, 'accounts/mypage.html', {
        'actions': actions,
        'rewards': rewards,
        'histories': histories,
        'points': points,
    })

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('mypage')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('mypage')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/signin.html', {'form': form})

@login_required
def signout(request):
    logout(request)
    return redirect('home')