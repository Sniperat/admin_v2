# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin


# Register your models here.
from django.contrib import admin
from .models import *
admin.site.register(Mahalla)
admin.site.register(User_info)
admin.site.register(Business)
admin.site.register(Farm)
