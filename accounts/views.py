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

    # ユーザーの利用開始日を取得 (例: User モデルに created_at フィールドがある場合)
    user_start_date = request.user.date_joined.date()  # Userモデルにdate_joinedがある場合

    # 今日を終了日に設定
    end_date = date.today()

    # 表示範囲の開始日を計算 (7日前)
    start_date = end_date - timedelta(days=6)

    # 利用開始日が7日前より前の場合、開始日を利用開始日に合わせる
    if user_start_date > start_date:
        start_date = user_start_date

    # 日ごとの累計ポイントを計算
    daily_points = []
    current_date = start_date
    cumulative_points = 0  # 累計ポイントを初期化

    # 利用開始日から過去7日間のデータを遡って累計ポイントを計算
    temp_date = user_start_date
    while temp_date < start_date:
        total_points_that_day = History.objects.filter(
            user=request.user,
            date=temp_date,
            action__isnull=False  # アクションのみを対象とする
        ).aggregate(Sum('point_change'))['point_change__sum'] or 0  # Noneの場合に0を返す

        cumulative_points += total_points_that_day
        temp_date += timedelta(days=1)

    while current_date <= end_date:
        # その日のアクションによるポイント合計を取得
        total_points_that_day = History.objects.filter(
            user=request.user,
            date=current_date,
            action__isnull=False  # アクションのみを対象とする
        ).aggregate(Sum('point_change'))['point_change__sum'] or 0  # Noneの場合に0を返す

        cumulative_points += total_points_that_day  # 累計ポイントを加算

        daily_points.append({
            'date': current_date.strftime('%Y-%m-%d'),
            'points': cumulative_points,  # 累計ポイントを記録
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