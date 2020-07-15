# django-tctip
一个 Django 应用，用来在页面显示打赏弹框，效果可看我博客 https://tendcode.com/

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
在需要展示的页面添加引入标签函数{% load tctip_tags %}，并添加标签函数{% load_tctip %}到html中，建议放在head标签末尾
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
    {% load_tctip %}
</head>
<body>
<div>django-tctip demo test !!!</div>
</body>
</html>

```

step 5
前往管理界面添加数据即可显示到前台（参数都是可以通过后台配置的，参数的作用可以查看前台注释中描述，比较简单故不做说明）

![](https://ftp.bmp.ovh/imgs/2020/07/471c08dcb08d47c0.png)

![](https://ftp.bmp.ovh/imgs/2020/07/cc4742af979cac9c.png)
![](https://ftp.bmp.ovh/imgs/2020/07/505d3218487e1114.png)

说明：django-tctip 是将tctip项目封装成了django的应用，感谢原项目 https://github.com/greedying/tctip 作者和删减版 https://github.com/HaddyYang/tctip 作者
