# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from django.views import View
from .form import MahallaForm, BussinessForm, FarmForm

from .models import Mahalla, User_info, Business, Farm


@login_required(login_url="/login/")
def index(request):
    user = User_info.objects.all()
    return render(request, "index.html", {'u': user})


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('error-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('error-500.html')
        return HttpResponse(html_template.render(context, request))


class Mahalla_view(View):
    def get(self, request):
        content = {
            'mahallalar': Mahalla.objects.all(),
            'form': MahallaForm()
        }
        return render(request, 'templatesMe/mahalla.html', content)

    def post(self, request):
        form = MahallaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mahalla')


def delete_mahalla(request, pk):
    print(pk)
    Mahalla.objects.get(id=pk).delete()

    return redirect('mahalla')


class Mahalla_update_view(View):
    def get(self, request, pk):
        content = {
            'mahalla': Mahalla.objects.get(id=pk),
            'form': MahallaForm(),
            'users':User_info.objects.all()
        }
        return render(request, 'templatesMe/mahalla_u.html', content)

    def post(self, request, pk):
        mah = Mahalla.objects.get(id=pk)
        mah.post_code = request.POST['post_code']
        mah.rais = User_info.objects.get(id=int(request.POST['rais']))
        mah.secretary = User_info.objects.get(id=int(request.POST['secretary']))
        mah.area = request.POST['area']
        mah.save()

        return redirect('update_mahalla', pk)




class Bussines_view(View):
    def get(self, request):
        content = {
            'bussines': Business.objects.all(),
            'form': BussinessForm()
        }
        return render(request, 'templatesMe/bussines.html', content)

    def post(self, request):
        form = MahallaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mahalla')
