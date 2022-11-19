# Graduater
## 全体像
**mac osの人**
1. docker desktopアプリを入れる
<br>
[ダウンロードリンク](https://www.docker.com/products/docker-desktop/)
2. このリポジトリをローカルの好きなフォルダにcloneする
<br>
```
git clone git@github.com:自分のgithubアカウント名/inet_b_treasure_map.git
```
例）
```
git clone git@github.com:ozuaq/inet_b_treasure_map.git
```

### **サイトにアクセス**
http://127.0.0.1:8000/inet_b_hackathon/treasure_map/zoom_out_map/

## Git
### **自分用のブランチを作ってコードを書いて、mainにマージし、問題がなければプルリクエストを送る**
※プルリクエストは後でみんなで知識共有します
<br>
例）
**自分のブランチを作る**
```
git branch ozaki_develop
```
**mainにマージする**
mainブランチにて
```
git merge ozaki_develop
```
### **非追跡ファイル設定**
- 開発メンバ共通で非追跡にしたいファイルの非追跡設定 <br>
.gitignoreに書く <br>
- 個人的なファイルの非追跡設定<br>
.git/info/excludeに書く <br>

## Django
### **フロントエンド**
- static/ <br>
css・image・jsファイルの配置場所
<br>
例）
<br>
static/css/sample.css
- template/ <br>
テンプレート(HTML)ファイルの配置場所
<br>
template/sample.html

### **バックエンド(あとで勉強したい人のため共有)**
- treasure_map/urls.py <br>
プロジェクトのURLを設定
- mysite/urls.py <br>
アプリのURL設定とmysite/views.py中のview関数と対応付け
- mysite/views.py <br>
データベースとのやりとり・必要な処理・次の遷移先ページといった内容を定義したview関数を書く
- mysite/models.py <br>
データベースのテーブルをclassとして定義

## 番外編 本番環境にデプロイする
**コンテナをバックグラウンドで起動**
```
docker-compose up -d
```
-d を付けるとコンテナをバックグラウンドで起動

**コンテナの停止**
```
docker-compose stop
```