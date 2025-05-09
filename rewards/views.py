from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Reward
from .forms import RewardForm

@login_required
def reward_list(request):
    rewards = Reward.objects.filter(user=request.user)
    return render(request, 'rewards/reward_list.html', {'rewards': rewards})

@login_required
def reward_create(request):
    if request.method == 'POST':
        form = RewardForm(request.POST)
        if form.is_valid():
            reward = form.save(commit=False)
            reward.user = request.user
            reward.save()
            return redirect('reward_list')
    else:
        form = RewardForm()
    return render(request, 'rewards/reward_create.html', {'form': form})

@login_required
def reward_update(request, pk):
    reward = get_object_or_404(Reward, pk=pk, user=request.user)
    if request.method == 'POST':
        form = RewardForm(request.POST, instance=reward)
        if form.is_valid():
            reward = form.save()
            return redirect('reward_list')
    else:
        form = RewardForm(instance=reward)
    return render(request, 'rewards/reward_update.html', {'form': form})

@login_required
def reward_delete(request, pk):
    reward = get_object_or_404(Reward, pk=pk, user=request.user)
    if request.method == 'POST':
        reward.delete()
        return redirect('reward_list')
    return render(request, 'rewards/reward_delete.html', {'reward': reward})