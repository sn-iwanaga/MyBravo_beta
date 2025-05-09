from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from actions.models import Action
from rewards.models import Reward
from histories.models import History
from django.db.models import Sum
from datetime import date, timedelta
import json

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



@login_required
def mypage(request):
    actions = Action.objects.filter(user=request.user)
    rewards = Reward.objects.filter(user=request.user)
    total_points = request.user.point

    # 今週の初日と最終日を計算
    today = date.today()
    start_date = today - timedelta(days=today.weekday())  # 週の開始日（月曜日）
    end_date = start_date + timedelta(days=6)  # 週の終了日（日曜日）

    # 今週の日ごとのポイント合計を計算
    daily_points = []
    current_date = start_date
    while current_date <= end_date:
        # その日のアクションによるポイント合計を取得
        total_points_that_day = History.objects.filter(
            user=request.user,
            date=current_date,
            action__isnull=False  # アクションのみを対象とする
        ).aggregate(Sum('point_change'))['point_change__sum'] or 0  # Noneの場合に0を返す

        daily_points.append({
            'date': current_date.strftime('%Y-%m-%d'),
            'points': total_points_that_day,
        })

        current_date += timedelta(days=1)

    # JSON 形式に変換
    daily_points_json = json.dumps(daily_points)

    return render(request, 'accounts/mypage.html', {
        'actions': actions,
        'rewards': rewards,
        'total_points': total_points,
        'daily_points': daily_points_json,  # グラフ用データを渡す
    })