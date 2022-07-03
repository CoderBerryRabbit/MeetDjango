#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : CoderBerryRabbit
# @Email    : CoderChaos@yeah.net
# @Time     : 2022/6/21 7:16
# @File     : urls.py python3.9
# @Software : PyCharm MeetDjango
# @Desc     : TODO

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
