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
from .form import MahallaForm, BussinessForm, FarmForm, UserForm

from .models import Mahalla, User_info, Business, Farm


@login_required(login_url="/login/")
def index(request):
    user = User_info.objects.all()
    form = UserForm()
    return render(request, "index.html", {'u': user, 'form': form})


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
            'users': User_info.objects.all()
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
        bussiness = BussinessForm(request.POST)
        if bussiness.is_valid():
            bussiness.save()
            return redirect('bussines')


def delete_bussines(request, pk):
    print(pk)
    Business.objects.get(id=pk).delete()

    return redirect('bussines')


class Bussiness_update_view(View):
    def get(self, request, pk):
        content = {
            'business': Business.objects.get(id=pk),
            'form': BussinessForm(),
            'users': User_info.objects.all()
        }
        return render(request, 'templatesMe/bussines_u.html', content)

    def post(self, request, pk):
        print(request.POST['owner'])
        user = User_info.objects.get(id=int(request.POST['owner']))
        mah = Business.objects.get(id=pk)
        mah.number = request.POST['number']
        mah.name = request.POST['name']
        mah.type = request.POST['type']
        mah.destination = request.POST['destination']
        mah.inn = request.POST['inn']
        mah.checking_account = request.POST['checking_account']
        mah.address = request.POST['address']
        mah.owner = user
        mah.phone_number = request.POST['phone_number']

        mah.save()

        return redirect('update_bussiness', pk)


class Farm_view(View):
    def get(self, request):
        content = {
            'farm': Farm.objects.all(),
            'form': FarmForm()
        }
        return render(request, 'templatesMe/farm.html', content)

    def post(self, request):
        farm = FarmForm(request.POST)
        if farm.is_valid():
            farm.save()
            return redirect('farm')


def delete_farm(request, pk):
    print(pk)
    Farm.objects.get(id=pk).delete()

    return redirect('farm')


class Farm_update_view(View):
    def get(self, request, pk):
        content = {
            'farm': Farm.objects.get(id=pk),
            'form': FarmForm(),
            'users': User_info.objects.all()
        }
        return render(request, 'templatesMe/farm_u.html', content)

    def post(self, request, pk):
        print(request.POST['owner'])
        user = User_info.objects.get(id=int(request.POST['owner']))
        mah = Farm.objects.get(id=pk)
        mah.number = request.POST['number']
        mah.name = request.POST['name']
        mah.area = request.POST['area']
        mah.inn = request.POST['inn']
        mah.checking_account = request.POST['checking_account']
        mah.address = request.POST['address']
        mah.owner = user
        mah.phone_number = request.POST['phone_number']

        mah.save()

        return redirect('update_farm', pk)


class User_view(View):
    def get(self, request):
        user = User_info.objects.all()
        form = UserForm()
        return render(request, "templatesMe/user.html", {'u': user, 'form': form})

    def post(self, request):
        farm = UserForm(request.POST, request.FILES)
        if farm.is_valid():
            farm.save()
            return redirect('user')



def delete_user(request, pk):
    print(pk)
    User_info.objects.get(id=pk).delete()

    return redirect('user')



class User_update_view(View):
    def get(self, request, pk):
        content = {
            'user': User_info.objects.get(id=pk),
            'form': UserForm(),
            'mahalla': Mahalla.objects.all()
        }
        return render(request, 'templatesMe/user_u.html', content)

    def post(self, request, pk):
        user = User_info.objects.get(id=pk)
        mah = Mahalla.objects.get(id=int(request.POST['mahalla']))
        user.mahalla = mah
        user.first_name = request.POST['first_name']
        user.second_name = request.POST['second_name']
        user.last_name = request.POST['last_name']
        # user.birth_date = request.POST['birth_date']
        user.sex = request.POST['sex']
        user.passport_data = request.POST['passport_data']
        user.inn = request.POST['inn']
        user.marital_status = request.POST['marital_status']
        user.actual_address = request.POST['actual_address']
        user.passport_address = request.POST['passport_address']
        user.work_status = request.POST['work_status']
        user.education = request.POST['education']
        # user.law_status = request.POST['law_status']
        user.mobile_phone = request.POST['mobile_phone']
        user.home_phone = request.POST['home_phone']
        user.work_phone = request.POST['work_phone']


        user.save()

        return redirect('update_user', pk)
