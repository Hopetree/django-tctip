# -*- coding:utf-8 -*-
# Author: https://github.com/Hopetree
# Date: 2020/7/11
from django import template
from ..models import Tip

register = template.Library()


@register.inclusion_tag('tctip/tips.html')
def load_tctip():
    tips = Tip.objects.filter(is_on=True)
    if tips:
        tip = tips[0]
    else:
        tip = None
    return {"tip": tip}
