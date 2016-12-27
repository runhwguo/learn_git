#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" url handlers """

import time
from www.coroweb import get
from www.models import Blog
from www.models import User

__author__ = 'RunhwGuo'


# 装饰器
@get('/')
# index = get('/)(index)
async def index(request):
    summary = '郭浩伟爱着程锡慧，他将会为了他们的家庭努力，好好工作，好好生活。'
    blogs = [
        Blog(id='1', name='Test Blog', summary=summary, created_at=time.time() - 120),
        Blog(id='2', name='Something New', summary=summary, created_at=time.time() - 3600),
        Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time() - 7200)
    ]
    return {
        '__template__': 'blogs.html',
        'blogs': blogs
    }


@get('/api/users')
async def api_get_users():
    users = await User.find_all(order_by='created_at desc')
    for u in users:
        u.passwd = '******'
    return dict(users=users)
