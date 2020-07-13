# Generated by Django 2.2.8 on 2020-07-13 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='默认提示栏', max_length=20, verbose_name='名称')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('is_on', models.BooleanField(default=True, verbose_name='是否使用')),
                ('headText', models.CharField(default='欢迎打赏支持本站 ^_^', max_length=20, verbose_name='最上面的文字')),
                ('siderText', models.CharField(default='公告＆打赏＆微信群', max_length=20, verbose_name='侧边栏文本')),
                ('siderTextTop', models.CharField(default='-72px', max_length=10, verbose_name='侧边栏文本高度调整')),
                ('siderBgcolor', models.CharField(default='#3a4c5b', max_length=30, verbose_name='侧边栏背景颜色')),
                ('siderTop', models.CharField(default='12%', max_length=10, verbose_name='侧边栏高度，可以px，em，或百分比')),
                ('buttomText', models.CharField(default='了解更多', max_length=10, verbose_name='底部文字')),
                ('buttomLink', models.CharField(default='https://github.com/Hopetree/django-tctip', max_length=100, verbose_name='底部文字链接')),
                ('notice_name', models.CharField(default='公告栏', max_length=10, verbose_name='公告栏名称')),
                ('notice_title', models.CharField(default='最新公告', max_length=20, verbose_name='公告栏标题')),
                ('notice_text', models.CharField(default='1. 最新公告<br>2. 公告换行', max_length=100, verbose_name='公告栏内容')),
                ('notice_flag', models.BooleanField(default=True, verbose_name='公告栏是否显示')),
                ('alipay_name', models.CharField(default='支付宝', max_length=10, verbose_name='支付宝栏名称')),
                ('alipay_title', models.CharField(default='扫描二维码打赏', max_length=20, verbose_name='支付宝栏标题')),
                ('alipay_desc', models.CharField(default='谢谢支持\n请用支付宝打赏', max_length=20, verbose_name='支付宝栏描述')),
                ('alipay_flag', models.BooleanField(default=True, verbose_name='支付宝栏是否显示')),
                ('alipay_qrimg', models.TextField(default='data:image/png;base64,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', verbose_name='支付宝栏二维码图片地址')),
                ('weixin_name', models.CharField(default='微信', max_length=10, verbose_name='微信栏名称')),
                ('weixin_title', models.CharField(default='扫描二维码打赏', max_length=20, verbose_name='微信栏标题')),
                ('weixin_desc', models.CharField(default='谢谢支持\n请用微信打赏', max_length=20, verbose_name='微信栏描述')),
                ('weixin_flag', models.BooleanField(default=True, verbose_name='微信栏是否显示')),
                ('weixin_qrimg', models.TextField(default='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAYAAADDPmHLAAAMv0lEQVR4Xu1dX4hcVxn/fXfuJBsstoI+VWlqRWoRTcUHwUoSae38W5OoYEWwrcb658WNRdruTOiWzKyRFk3Al2JLUxBJJSUbdv5sS6WpJkVB6SY+BQrdPgh9EJINYtPszP3kzM4kk5l755xz752Zc52zjzvf+c7353e/8/f7DsH+TbUFaKq1t8rDAmDKQWABYAEw5RaYcvVtBLAAmHILTLn6NgJYAOhbIN+YfwBEnwHjDgLdqs/BvwUz30JEO3T4MfBPB/QPJu8KmC56Ke+P9a8trurwUKXNvTq/g1q4E45zh+PRp1TbyegY+BjAH5LR9f3uAmgyvH+D8FeHnAvL95ermjz0loGZV5/Iuc3UoyB8VbejMdKvg/nPvMV5unbvob/E0e/sK6UCM34Axm4AN8fBcxQ8mLAClxZ19FYeAvIrpcPE+LHJBug1KgOXibxHq5nF56IYO2l6A1hvOfyjxv2Vl1T0VgJAoVEsAXRIhaFhNOsEPLWcLf8mjFyztYO/ZIcfD9N2wm2UQSAFwDf+VL7tg6tXzhDw8QkrFbJ7vtBEK7OSPbymw6Ad9j38PikRr183Bv6ennHvW9q9cGmY3lIAdELgYzrGM42WPDq8nD/0hI5chXrxeRB9X6eNabQeeT+sS4ZAOQDqpTNE+LKvcoyjICyZoDgzi9XDHBHd5vM1nK1ly/eoyplpPL7dQarmgO4a4MX8LhMvOHC0Iopq39p0jL1M/BCBBianHnkv1zOL34oUAQqNkgghA8yJsW85VzbC+V0F976+cMvG+xurPiBY91LeLtXlYaFR2gXgdT/np7eld8jCqrYTIzYIkhfgC9Vs5c6oAGA/BtVsWRo9IuoVqnmhXjoNwk6fxrur2fJpFaa5lfn9Dju/G6BlHK3mynMqPMZNU2iUQvlJ6sSwjMdtgG5/cQAgv1KcIya/lcNT1Wx5YVK6Des3rJ8sAHysagHQY5SwyJrUV2IjwI2Wlw3VNgLYCDD8W7UR4Ab72DlA1xyy0GKHgPFaIOyHaocAOwTYIaDfAnGuAsTmVOv91ud14sFy7tAbOvSCNhERQGyxpjk9sFUbpGwoQ8SwERQXAHKN+YccOC/oOpPBa5zifao7l8YDQHwFzSvNkwDEFqv6H+OSR96BenbxmGojU5aBHZ0vqsrdT8fMq7Vc5W7V9kZHgHyjeIxAD6oq00/XRPN21eNcUwAQvD+vbgWdibbRACjUSxdBuEVd9QFK5X18CwADN4KC0KkBCAsAibHMjgABJ1UWAMMt8P8zBFgAaGD9OqkFwHVb2CHADgFqlznsJNBOAiPfCIpjI8guA3uAaFcBoaYAsHMAOweQHtZ1TWSXgR1L2DmAnQMYMQcYdkCjMiAweL2WrSjvnhodAfKN4hKB9qgoHkCTuGWg0CNfL4pElVB5iR68h7UOwUy+Fh5xRnyumi0r1wwwZQjoAlnUFHBazl5V8DPzpRa1llQPvxIxBxBCirsALtyHVA0h6Dx4azpfQTvsGnQfQEfXqLRGDwFRldNpbwFg4CRQx4FRaS0ALACMWQVEBbNOezsEGLYPoOO8OGgtACwAbHawXQUMxhLZeYJ0rzlsaIkjrIXhEccksF0Or5Wq+fQ/falh+fr8q0TOff3GcGfcj5hWKaOz+/ZWQLFJ9d3EoAoh4FO1bEV5UycMgMO06eyxvNPflpn/VctVhhb3kkaA2UbpGAN+V7pPuzPuPlNA0CkP8yQR+VXwuOylvJ2qiRYdXm+SqIba/0eYq2bKR8M4ahRthPNTnDrpC3rCH6qZ8neH9SsFQGFlfj/8yqV0uIoEBiIaWopsFIr38pSVmGVAq0jU5lzi4AkQfzNIdiP0Bm8n0PYgGQn4uaxGohQAmxkuG+cB+sSoHTkq/kx8oJapHNHhn6/PP0LkPKvTxiRaEf5b1LpHdqYgBYBQKrBokkkaB8jigZe3zKS/pztUtYeBKxvHCXR/AtT0EZEPVrOVskx2JQBshsTkFU5k9v7W2oJHVu5dPC8zhN/vmdfmP5e6Ssd95wJhGI6pDYOfr2Ur+1W6UwZAe4a9WTD6JwA+rMJ8UjTiMoUDWtpAc0EWAmUyChCkrzoVJhRktJP+XYR9OHhGZ7jTAkAbBK8d/Ao2vK8D+CIRfRSMz05ccfA6mN5mx1sj8Hm47us6JdNV5BdvJDhwMuxhBxxo5fur8A9Jcxke3gHR20R8dgPNk7qA1wZAv6CdCw/KV5dCKjq0mWoByLj67qy7A2ffcfUj49NEc03X4f08IwNAJqT93WwLWACY7Z+RS2cBMHITm92BBYDZ/hm5dBYAIzex2R1YAJjtn5FLZwEwchOb3YEFgNn+Gbl0FgAjN7HZHRgNgNn6Qb+nX9oWbbmtddULHma7YLLShQKAeFPPY+9uh1Of9NC6CXC2E/AfuSo8A6KZQDpu81B+3QvAGRBuEvwYeM9heo+pddbduuWE7vGvXPZNis7W9x4QLrlb3Rej9pNbKe5xmHZ4xKv1TOWUqhyCThxZX/1gY2e7fco7FeaD0ALA5qPRzoPk4UsRCz/q6KlNKx5NJPKejfpsbH/HhXrpCAg/u/Z/UcrW9XaHMbzgkW8UXyDQtXxJccsovS29WwVUnfsKb/XeCGLwsVq28rCOwZQBkMA3dMGEX6W3uodVDKpiNL8b0gx+sZataCW99kSSt/r7VU0LD0o991Le3TqAVAJA+16g5zxt8lcf7EC1mzEyAASmuDPeqObKekWwN8u7i9fHnvTpV+nq+ZD6y8q3n0XfUgAMe0VTZjRDfl/nNM1GvR9gGgDiyH9QAoDsVrAhTh4qBoOfqWUrv4giq2kAGFJ1Jd4IUKiXjoPw7X7jMfO7Dmhug5qrUS8lRHFMt62YnVOLFgJK0WhVGfGTxzQAjC8CBLwdrDvZiMPJKjzy9eKa3wPSALS+jIEVQEC2ECY0BxgnAEJlnao4axQ0cRnGAqBjgWlMDrVDQI8FLAA2jWHaHGB8k8CQ9edGEd5VeI5qCBB95xvFSwS6uVeOsBtBUfcB/AAp8iHSM+ntOhtf0n0AGwGuu1s8A0egIz0gOOfOuLt0DN7lFhUAgs9svbTXAx8Rk14Gn+IUL+jsAqrtA9gIcEPg6c0JcGfc1TDO7wwpkXYCVaKhCo2NACpWGgFNHBEgDrEsAOKwYggeFgAhjKbSZJSTQJX+VWmGFJJWOgxS7UdGN7YIIGatzLwnoH7PgJzibByE1Vq28qJMid7fkwKAzsWS0MfBOjYZRjsWAIR9RLktOGOpmivvU1V4lABo1+NBShzh7iLQGghLUeoF+Rzpaq0qOquAJ8WlECZeaqH1lO65zFgAEPXpWJ1zh1ECIF8vDlQgU73AEQTgbjl5Yqwu58pLqkAXzmeCeJD72p94dbyWrdyuymNsy8CkPRrlZ8CgUmxhD4N0nORHO3A97TqR1qHXeCJAwl4O9TV4zKeBMQAgclFsGwE0vBD3WYBG176kcQ11NgIoesICoM9QsiLENyzN7BAQCLNuXoDIM9BZUdgIEGDSuAzTz34UEaBQL50E4VrtYZ28gLj0tEPAhIaAIEAx84FaTl7V1AIg4REg6lawBUDCARD1MMgCwAIgOfsAQ65qK47A6le64/oyRj0JnKoIMCSPTQoA3XtuFgDqH8vYdgLbbw6831wCIbDggx8SutlHOockFgAGAsDPuX41huOofTtFALixVoHJh0HSOB8jwdQAIDi93LzTwBj9K2VlAZCQIUDqyZAEFgAWALGsj41fBtohwD9E2AhgI4CNANnyadURdCyngarCxEFnI0DMESDfKF4g0Kd9nKO13IjDuTIefrXzetpEkjfu+wCRt4LHNQfIrcyfcNgZfEKVcYmJ59Iz6VNhEyRlDtX5XdysIQ8Lfoknqq9oDutvagFQaBRLAB3ScYZptAx+pZatZKLINbUA6LxOfYaIbo1iwEm2ZXjfqWUXj0eRYWoBIIw22ygdYODXUQw4sbaMl6q58gNR+w/K5QubGDIkXU4pOXTIHEJrriNdBQjDbZ7mtZ4b9px6VAOPpD3Ty+621P645ih+JWIAKDmsX7/ATCPFcnZBAGqiebtOfqASALogaP239Rg7/FPT3w4GcA7gE+5M+rdxOV/YoJ3hDF66ViKG8Ya7zd0bto+BkjOMo9VceU71Y+hNDxP3Jhg8V88uHlNtL+iUAdBl2jYCIQPP+wJAd12bG3jC6BP6c9qKrHqMyyDvzfTMlpWwTlHRQHy9Ol+ZjKewadhyM92SNWGfz9UGgEwZ+3uyLGABkCx/xS6tBUDsJk0WQwuAZPkrdmktAGI3abIYWgAky1+xS2sBELtJk8XQAiBZ/opdWguA2E2aLIYWAMnyV+zSWgDEbtJkMfwfO0cuF3rAnEoAAAAASUVORK5CYII=', verbose_name='微信栏二维码图片地址')),
                ('wechat_name', models.CharField(default='微信群', max_length=10, verbose_name='微信群栏名称')),
                ('wechat_title', models.CharField(default='扫描二维码进群', max_length=20, verbose_name='微信群栏标题')),
                ('wechat_desc', models.CharField(default='加入微信群\n获取更多信息', max_length=20, verbose_name='微信群栏描述')),
                ('wechat_flag', models.BooleanField(default=True, verbose_name='微信群栏是否显示')),
                ('wechat_qrimg', models.TextField(default='data:image/png;base64,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', verbose_name='微信群栏二维码图片地址')),
            ],
            options={
                'verbose_name': '公告栏',
                'ordering': ['-create_date'],
                'verbose_name_plural': '公告栏',
            },
        ),
    ]
