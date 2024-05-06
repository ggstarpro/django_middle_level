# 概要
[【中級者向け・Django4対応】Python/DjangoによるECサイト開発講座（Django3.2系にも対応）](https://www.udemy.com/course/django-ecweb-vegeket/?couponCode=KEEPLEARNING)

# 参考
[GitHub](https://github.com/takux/vegeket_project)
[Qiita](https://qiita.com/takux)
[blog](https://www.rabbitriver.page/ja/)

# 環境構築
`$ python3 -m venv venv`
`$ source venv/bin/activate`

`$ pip install Django==`
`$ pip install --upgrade "Django==4.0.*" `
`$ pip show Django`

`$ django-admin startproject config .`
`$ python manage.py startapp base`


# フォルダ作成
- base/
- secrets/
    - .env.example
    - .env.dev
    - .env.prod
- static/
- templates/
- config/
- venv/
- mamage.py

# settings.py修正
- `SECRET_KEY`の記述はgithubに上げないようにしてください
- `INSTALLED_APPS`に`'base,'`を追加
- `TEMPLATESのDIRS`に`[BASE_DIR / 'templates']`を追加
- `LANGUAGE_CODE = 'ja'`に変更
- `TIME_ZONE = 'Asia/Tokyo`に変更
- `STATICFILES_DIRS = [BASE_DIR / 'static']`

# django-environ
`$ pip install django-environ==0.4.5`
`$ pip freeze > requirements.txt`

# 画像を扱う Pillow
`$ pip install Pillow`

# DB
`$ python manage.py makemigrations`
`$ python manage.py migrate`

# 管理画面
`python manage.py createsuperuser`
```
ユーザー名 (leave blank to use 'gm'): test
メールアドレス: test@example.com
Password: password
Password (again): password
このパスワードは一般的すぎます。
Bypass password validation and create user anyway? [y/N]: y
```

# 立ち上げ
`$ python manage.py runserver`


# shell
`$ python manage.py shell`
```
>>> class Test:
...     pass
...
>>> t = Test()
>>> t
<Test object at 0x103cfd130>
>>> print(t)
<Test object at 0x103cfd130>


>>> class Test2:
...     def __str__(self):
...         return "これはテストです"
...
>>> t2 = Test2()
>>> t2
<Test2 object at 0x103cfd430>
>>> print(t2)
これはテストです
```


# メモ
## クラスビュー
- ListView