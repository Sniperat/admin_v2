# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
from .views import Mahalla_view, delete_mahalla, Mahalla_update_view, Bussines_view, delete_bussines, Bussiness_update_view, Farm_view, delete_farm, Farm_update_view

urlpatterns = [
    # Matches any html file 
    re_path(r'^.*\.html', views.pages, name='pages'),

    # The home page
    path('', views.index, name='home'),
    path('mahalla/', Mahalla_view.as_view(), name='mahalla'),
    path('bussines/', Bussines_view.as_view(), name='bussines'),
    path('farm/', Farm_view.as_view(), name='farm'),
    path('mahalla_d/<int:pk>', delete_mahalla, name='delete_mahalla'),
    path('bussines_d/<int:pk>', delete_bussines, name='delete_bussines'),
    path('farm_d/<int:pk>', delete_farm, name='delete_farm'),
    path('mahalla_u/<int:pk>', Mahalla_update_view.as_view(), name='update_mahalla'),
    path('mbussines_u/<int:pk>', Bussiness_update_view.as_view(), name='update_bussiness'),
    path('farm_u/<int:pk>', Farm_update_view.as_view(), name='update_farm')
]
