# django-tctip
一个 Django 应用，用来在页面显示打赏弹框

step 1
安裝包
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
在需要展示的页面添加引入标签函数，并添加标签函数到html中
```html
{% load tctip_tags %}
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="referrer" content="origin">
    <title>Title</title>
</head>
<body>
<div>django-tctip demo test !!!</div>
{% load_tctip %}
</body>
</html>

```

step 5
前往管理界面添加数据即可显示到前台

说明：django-tctip 是将tctip项目封装成了django的应用，感谢原项目https://github.com/greedying/tctip作者和删减版作者