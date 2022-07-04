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

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
