# MyBravo 導入ドキュメント

このドキュメントでは、MyBravoを他の人が利用できるようにするための導入手順を説明します。

**前提条件:**

*   MyBravoのソースコードが共有されていること (GitHubなどのプライベートリポジトリ)
*   MyBravoで使用しているPythonのバージョンがインストールされていること (推奨バージョン: Python 3.9以上)
*   Gitがインストールされていること

**1. 環境構築**

1.  **リポジトリのクローン:**

    *   ターミナルまたはコマンドプロンプトを開き、MyBravoのリポジトリをクローンします。

        ```bash
        git clone https://github.com/sn-iwanaga/MyBravo.git
        cd MyBravo
        ```

2.  **仮想環境の作成 (推奨):**

    *   プロジェクトごとに依存関係を分離するために、仮想環境を作成します。

        ```bash
        python -m venv venv  # "venv" は仮想環境の名前 (任意)
        ```
3.  **仮想環境の有効化:**

    *   Windowsの場合:

        ```bash
        venv\Scripts\activate
        ```

    *   macOS/Linuxの場合:

        ```bash
        source venv/bin/activate
        ```
4.  **必要なパッケージのインストール:**

    *   `requirements.txt` ファイルに、MyBravoに必要なパッケージがリストされています。 以下のコマンドを実行して、必要なパッケージをインストールします。

        ```bash
        pip install -r requirements.txt
        ```

**2. アプリケーションの設定**

1.  **データベースの設定:**
    *   PostgreSQLサーバーを起動し、MyBravo用のデータベースとユーザーを作成してください。
    *   その後`settings.py` ファイルで、`DATABASES` の `ENGINE` を `'django.db.backends.postgresql_psycopg2'` に設定し、`NAME`, `USER`, `PASSWORD`, `HOST`, `PORT` を作成したデータベースに合わせて変更してください。

2.  **マイグレーションの実行:**

    *   データベースのスキーマを最新の状態に更新するために、マイグレーションを実行します。

        ```bash
        python manage.py migrate
        ```

3.  **スーパーユーザーの作成 (必要な場合):**

    *   管理サイトにアクセスするために、スーパーユーザーを作成します。

        ```bash
        python manage.py createsuperuser
        ```

**3. アプリケーションの実行**

1.  **開発サーバーの起動:**

    *   開発環境では、Djangoの開発サーバーを使用できます。

        ```bash
        python manage.py runserver
        ```

    *   ブラウザで `http://127.0.0.1:8000/` にアクセスして、MyBravoが動作することを確認します。

2.  **初期設定:**
アカウント登録を行ってください
3.  **アクションの追加:**
画面右上のAction Settingsからアクションを追加できます
4.  **開発サーバーの起動:**
画面右上のReward Seggingsからご褒美を追加できます
5.  **記録:**
Actionの実行やRewardとの交換はメインページから行えます