# Djangoで作るシンプルなブログ

## はじめに
[ヨコハマDjango勉強会](https://connpass.com/event/73811/)のためのサンプルです。  
月1回くらいのペースで開催しようと思っています。  
ヨコハマにPython&Djangoコミュニティができればいいな。

このサンプルではDjango2.0を使っています。  
[Django 2.0 release notes](https://docs.djangoproject.com/en/2.0/releases/2.0/)

## 動かし方

### まずはDjangoをインストール
virtualenvなどで仮想環境つくっておくとよいかも。

`pip install django`

### データベースの初期化
SQLiteで自動的にDBが作成されます。

`python manage.py migrate`

### スーパーユーザーの作成
Django管理画面にログインするためのスーパーユーザーを登録します。

`python manage.py createsuperuser`

### サーバーを起動
Djangoの簡易サーバーを起動します。
`python manage.py runserver`

デフォルトだと8000番ポートが使用されます。

もし他のポートがよければ

`python manage.py runserver localhost:8010`

とかやればOK。

## ゼロから作りたい人向けのメモ
### プロジェクトを作成
`django-admin startproject [projectname]`
### プロジェクト内にアプリを作成
`python manage.py startapp [appname]`

## 便利ツール
* [Cookiecutter Django](https://github.com/pydanny/cookiecutter-django)  
DockerとかgulpとかコミコミでDjangoプロジェクトの雛形を生成してくれる。
* [Awesome Django](https://github.com/rosarior/awesome-django)  
便利なDjango Appsのリスト。きちんとメンテナンスされているAppsを厳選している。