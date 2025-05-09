from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from actions.models import Action
from rewards.models import Reward
from .models import History
from django.contrib import messages

@login_required
def record_action(request, action_pk):
    action = get_object_or_404(Action, pk=action_pk, user=request.user)
    user = request.user

    # 現在のポイントを取得
    current_total_points = user.point

    # ポイントを加算
    point_change = action.points
    user.point += point_change
    user.save()

    # 履歴を作成
    History.objects.create(
        user=user,
        action=action,
        point_change=point_change,
        current_total_points=current_total_points + point_change # 加算後のポイントを記録
    )

    messages.success(request, f"{action.action_name}を記録しました。{point_change}ポイント獲得！")
    return redirect('mypage')

@login_required
def exchange_reward(request, reward_pk):
    reward = get_object_or_404(Reward, pk=reward_pk, user=request.user)
    user = request.user

    # 現在のポイントを取得
    current_total_points = user.point

    # ポイントが足りるか確認
    if user.point < reward.required_points:
        messages.error(request, "ポイントが足りません。")
        return redirect('mypage')

    # ポイントを減算
    point_change = -reward.required_points
    user.point += point_change
    user.save()

    # 履歴を作成
    History.objects.create(
        user=user,
        reward=reward,
        point_change=point_change,
        current_total_points=current_total_points + point_change # 減算後のポイントを記録
    )

    messages.success(request, f"{reward.reward_name}と交換しました。{reward.required_points}ポイント消費。")
    return redirect('mypage')