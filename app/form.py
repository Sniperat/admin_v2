from django import forms
import re
from django.forms import widgets
from .models import Mahalla, Business, Farm


class MahallaForm(forms.ModelForm):
    class Meta:
        model = Mahalla
        fields = ('post_code', 'name', 'rais', 'secretary', 'area')

        # widgets = {
        #     'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'phone': forms.TextInput(attrs={'class': 'form-control'}),
        # }

    # def clean_phone(self):
    #     phone_len = [12, 13]
    #     phone = self.cleaned_data.get('phone')
    #     if '+998' or '998' in phone:
    #         if len(phone) in phone_len:
    #             return phone
    #     raise forms.ValidationError('неправильный формат номера телефона')
    #
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if not '@' in email:
    #         raise forms.ValidationError('электронная почта недействительна')
    #     return email


class BussinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = '__all__'


class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = '__all__'
