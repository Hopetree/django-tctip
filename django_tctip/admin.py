from django.contrib import admin
from .models import Tip


# Register your models here.

@admin.register(Tip)
class TipAdmin(admin.ModelAdmin):
    fieldsets = (
        ('基本设置', {'fields': (('is_on',),
                             ('name', 'minScreenSize'),
                             ('headText', 'siderText'),
                             ('siderTextTop', 'siderBgcolor', 'siderTop'))}),
        ('公告栏设置', {'fields': (('notice_flag',),
                              ('notice_name', 'notice_title'),
                              ('notice_text',))}),
        ('支付宝栏设置', {'fields': (('alipay_flag',),
                               ('alipay_name', 'alipay_title'),
                               ('alipay_desc', 'alipay_qrimg'))}),
        ('微信栏设置', {'fields': (('weixin_flag',),
                              ('weixin_name', 'weixin_title'),
                              ('weixin_desc', 'weixin_qrimg'))}),
        ('微信群设置', {'fields': (('wechat_flag',),
                              ('wechat_name', 'wechat_title'),
                              ('wechat_desc', 'wechat_qrimg'),
                              ('wechat_icon',))})
    )
