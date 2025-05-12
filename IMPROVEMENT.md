# HISTORY: 複合キーを使用する＋削除ではなく無効化

## 現在の設計

```mermaid
erDiagram
    USER {
        int id PK
        varchar username
        varchar password
        varchar email
        datetime date_joined
        int point
    }

    HISTORY {
        int id PK
        int user_id FK
        int action_id FK
        int reward_id FK
        date date
        int point_change
        int current_total_points
        datetime created_at
    }

    ACTION {
        int id PK
        varchar action_name
        int point
    }

    REWARD {
        int id PK
        varchar reward_name
        int point
    }

    USER ||--o{ HISTORY : has
    HISTORY }o--|| ACTION : uses
    HISTORY }o--|| REWARD : uses
```

### 説明

*   **USER**: ユーザー情報を保持
*   **HISTORY**: ポイントの変動履歴を保持。どのアクションまたはリワードによってポイントが変動したかを記録。
*   **ACTION**: ユーザーが実行できるアクションを定義。
*   **REWARD**: ユーザーが獲得できるリワードを定義。

## 改善案

```mermaid
erDiagram
    USER {
        int id PK
        varchar username
        varchar password
        varchar email
        datetime date_joined
        int point
    }

    HISTORY {
        int id PK
        int user_id FK
        datetime date
        int point_change
        varchar related_object_type
        int related_object_id
    }

    ACTION {
        int id PK
        varchar action_name
        int point
        boolean is_deleted
    }

    REWARD {
        int id PK
        varchar reward_name
        int point
        boolean is_deleted
    }

    USER ||--o{ HISTORY : has
    HISTORY }o--|| ACTION : uses
    HISTORY }o--|| REWARD : uses
```

### 説明

*   **USER**: ユーザー情報を保持。
*   **HISTORY**: ポイントの変動履歴を保持。`related_object_type`と`related_object_id`を使用して、どのアクションまたはリワードによってポイントが変動したかを記録。
*   **ACTION**: ユーザーが実行できるアクションを定義。`is_deleted`フラグで削除フラグを管理。
*   **REWARD**: ユーザーが獲得できるリワードを定義。`is_deleted`フラグで削除フラグを管理。

### 変更点

*   `HISTORY`テーブルから`action_id`と`reward_id`を削除し、代わりに`related_object_type`と`related_object_id`を追加。これにより、常に`action_id`もしくは`reward_id`のどちらかが`NULL`になる状態を回避できる。
*   `ACTION`と`REWARD`テーブルに`is_deleted`カラムを追加。これにより、アクションやリワードを削除しても履歴に残る。

### 変更することによるメリット
*  actionやrewardを削除（無効化）してもHISTORYテーブルでそれを参照できる
*  NULLが消えるため美しい