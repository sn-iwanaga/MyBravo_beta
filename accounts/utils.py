import matplotlib.pyplot as plt
import io
import base64

def generate_weekly_point_chart(daily_points):
    """
    日ごとのポイントデータを受け取り、matplotlibで折れ線グラフを生成し、
    base64エンコードされたPNG画像を返す。
    """
    dates = [entry['date'] for entry in daily_points]
    points = [entry['points'] for entry in daily_points]

    plt.figure(figsize=(10, 6))  # グラフのサイズを調整
    plt.plot(dates, points, marker='o')
    plt.xlabel('Date')
    plt.ylabel('Points')
    plt.title('Weekly Point Chart')
    plt.xticks(rotation=45)  # X軸のラベルを回転
    plt.tight_layout()  # ラベルが重ならないように調整

    # グラフをPNG画像としてメモリに保存
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    # PNG画像をbase64エンコード
    image_png = buffer.getvalue()
    chart = base64.b64encode(image_png).decode('utf-8')

    return chart