# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
from .views import Mahalla_view, delete_mahalla, Mahalla_update_view

urlpatterns = [
    # Matches any html file 
    re_path(r'^.*\.html', views.pages, name='pages'),

    # The home page
    path('', views.index, name='home'),
    path('mahalla/', Mahalla_view.as_view(), name='mahalla'),
    path('mahalla_d/<int:pk>', delete_mahalla, name='delete_mahalla'),
    path('mahalla_u/<int:pk>', Mahalla_update_view.as_view(), name='update_mahalla')
]
