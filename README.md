# django-tctip
一个 Django 应用，用来在页面显示打赏弹框

step 1
```bash
pip install django-tctip
```

step 2
配置中添加应用
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_tctip',
]
```

step 3
生成数据表
```bash
python manage.py makemigrations
python manage.py migrate
```

step 4
前往管理界面添加数据即可显示到前台