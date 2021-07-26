from django.db import models
from django.contrib.auth.models import User



class User_info(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='avatars/')
    birth_date = models.DateField()
    sex = models.CharField(max_length=5)
    passport_data = models.CharField(max_length=9)
    inn = models.CharField(max_length=10, null=True)
    marital_status = models.CharField(max_length=10)  # TODO Choose bo'lishi kerak
    actual_address = models.CharField(max_length=50, default=None)
    passport_address = models.CharField(max_length=50)
    work_status = models.CharField(max_length=50)
    education = models.CharField(max_length=50, blank=True, null=True)
    law_status = models.BooleanField()
    mobile_phone = models.CharField(max_length=14)
    home_phone = models.CharField(max_length=14)
    work_phone = models.CharField(max_length=14)
    mahalla = models.ForeignKey("Mahalla", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.second_name}"


class Mahalla(models.Model):
    post_code = models.CharField(max_length=6)
    name = models.CharField(max_length=255)
    rais = models.OneToOneField(User_info, on_delete=models.CASCADE, related_name='mahalla_boss')
    secretary = models.OneToOneField(User_info, on_delete=models.CASCADE, related_name='mahalla_kotiba')
    area = models.IntegerField()


class Farm(models.Model):
    number = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    area = models.IntegerField()
    inn = models.CharField(max_length=10, null=True)
    checking_account = models.IntegerField()
    address = models.CharField(max_length=155)
    owner = models.ForeignKey(User_info, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=14)


class Business(models.Model):
    number = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    destination = models.CharField(max_length=255)
    inn = models.CharField(max_length=10, null=True)
    checking_account = models.IntegerField()
    address = models.CharField(max_length=155)
    owner = models.ForeignKey(User_info, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=14)

#
# # информация об образовании
# class Education(models.Model):
#     education_info = models.ForeignKey(User_info, on_delete=models.CASCADE)
#     education_type = models.CharField(max_length=50)
#     name = models.CharField(max_length=50)
#     faculty = models.CharField(max_length=50)
#     start_date = models.CharField(max_length=12)
#     finish_date = models.CharField(max_length=12)
#
#     def __str__(self):
#         name_split = self.education_info.full_name.split(' ')
#         return f'{name_split[0]}  {self.education_info.passport_data}'
#
#
# # информаци о судимости
# class User_law_info(models.Model):
#     User_law_info = models.ForeignKey(User_info, on_delete=models.CASCADE)
#     law_num = models.CharField(max_length=50)
#     date = models.CharField(max_length=12)
#
#
# # информаци о сожителе
# # class User_housemate(models.Model):
# #     User_housemate = models.ManyToManyRel(User_info)
#
#
# # номер пользователя
# # class User_housemate_tel(models.Model):
# #     User_housemate_tel = models.ForeignKey(User_housemate, on_delete=models.CASCADE)
# #     phone_tel = models.CharField(max_length=13)
#
#
# # информация об имуществе
# class Property_info(models.Model):
#     Property_info = models.ForeignKey(User_info, on_delete=models.CASCADE)
#     adress = models.CharField(max_length=50)
#     kadastr_number = models.CharField(max_length=20)
#     kadastr_sum = models.CharField(max_length=20)
#     economic_num = models.CharField(max_length=20)
#     floor = models.CharField(max_length=2)
#     total_area = models.CharField(max_length=50)
#     house_area = models.CharField(max_length=50)
#     living_room = models.CharField(max_length=50)
#     extra_info = models.CharField(max_length=50)
#     property_type = models.CharField(max_length=50)
#     register_number = models.CharField(max_length=50)
#     register_date = models.CharField(max_length=12)
#     foundation_documents = models.FileField()
#     kadastr_copy = models.FileField(upload_to='files/')
#     kadastr_contract_number = models.CharField(max_length=50)
#     kadastr_contract_date = models.CharField(max_length=12)
#
#     # garden_area = models.CharField(max_length=50)
#
#     def __str__(self):
#         return f'{self.Property_info.full_name}  {self.kadastr_number}'
#
#
# # фотографии имущества
# class Property_photo(models.Model):
#     Property_photo = models.ForeignKey(Property_info, on_delete=models.CASCADE)
#     photo = models.ImageField(upload_to='property_photos/')
#
#     def __str__(self):
#         # name_split=self.Property_photo.Property_info.full_name.split(' ')
#         return f'{self.Property_photo}  '
#
#
# #
# class Tex_info(models.Model):
#     Tex_info = models.ForeignKey(Property_info, on_delete=models.CASCADE)
#     build_date = models.CharField(max_length=12)
#     floor_count = models.CharField(max_length=50)
#     wall_material = models.CharField(max_length=50)
#     electricity = models.BooleanField()
#     gas = models.BooleanField()
#     water = models.BooleanField()
#     heating = models.BooleanField()
#     water_2 = models.BooleanField()
#     communication = models.BooleanField()
#     lift = models.BooleanField()
#
#     def __str__(self):
#         return f'Техническая информация  {self.Tex_info.kadastr_number}  '
#
#
# #
# class Room_info(models.Model):
#     Room_info = models.ForeignKey(Property_info, on_delete=models.CASCADE)
#     type = models.CharField(max_length=50)
#     room_area = models.CharField(max_length=50)
#
#
# #
# class Garden_info(models.Model):
#     Garden_info = models.ForeignKey(User_info, on_delete=models.CASCADE)
#     area = models.CharField(max_length=50)
#
#
# #
# class Plant_type_doc(models.Model):
#     Plant_type_doc = models.ForeignKey(Garden_info, on_delete=models.CASCADE)
#     type = models.CharField(max_length=50)
#     count = models.CharField(max_length=50)
#
#
# #
# class Plant_type_fact(models.Model):
#     Plant_type_fact = models.ForeignKey(Garden_info, on_delete=models.CASCADE)
#     type = models.CharField(max_length=50)
#     count = models.CharField(max_length=50)
#
#
# #
# class Planting_plan(models.Model):
#     Planting_plan = models.ForeignKey(Garden_info, on_delete=models.CASCADE)
#     type = models.CharField(max_length=50)
#     count = models.CharField(max_length=50)
