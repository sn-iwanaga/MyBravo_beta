from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Action
from .forms import ActionForm

@login_required
def action_list(request):
    actions = Action.objects.filter(user=request.user)
    return render(request, 'actions/action_list.html', {'actions': actions})

@login_required
def action_create(request):
    if request.method == 'POST':
        form = ActionForm(request.POST)
        if form.is_valid():
            action = form.save(commit=False)
            action.user = request.user
            action.save()
            return redirect('action_list')
    else:
        form = ActionForm()
    return render(request, 'actions/action_create.html', {'form': form})

@login_required
def action_update(request, pk):
    action = get_object_or_404(Action, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ActionForm(request.POST, instance=action)
        if form.is_valid():
            action = form.save()
            return redirect('action_list')
    else:
        form = ActionForm(instance=action)
    return render(request, 'actions/action_update.html', {'form': form})

@login_required
def action_delete(request, pk):
    action = get_object_or_404(Action, pk=pk, user=request.user)
    if request.method == 'POST':
        action.delete()
        return redirect('action_list')
    return render(request, 'actions/action_delete.html', {'action': action})