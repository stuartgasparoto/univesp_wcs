import email
from pyexpat import model
from venv import create
from django.db import models
from django.contrib.auth.models import User

## Tabela de clientes
class Customer (models.Model):
    name = models.CharField("Customer Name",max_length=256)
    ## Armazenar UserID da tabela de usuários padrão do Django
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ## Armazenar data de criação e atualização (automática pelo Django)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

## Tabela de contatos
class Contact (models.Model):
    CONTACT_TYPE_CHOICES = [
        ('1', 'Dono/Fazendeiro'),
        ('2', 'Gerente de Fazenda'),
        ('3', 'Parente'),
        ('4', 'Outros')
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    contact_type = models.IntegerField(choices=CONTACT_TYPE_CHOICES)
    name = models.CharField("Contact Name",max_length=256)
    cellphone = models.CharField(max_length=15)
    email = models.EmailField()
    main_contact = models.BooleanField()
    ## Armazenar data de criação e atualização (automática pelo Django)
    createad = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

## Tabela com informações sobre as "plantações"
class Plant (models.Model):
    name = models.CharField(max_length=128)
    water_per_day = models.FloatField("Recommended water volume per day (mm)")
    ## Armazenar data de criação e atualização (automática pelo Django)
    createad = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Farm (models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    address = models.CharField(max_length=512)
    number = models.IntegerField()
    cep = models.IntegerField()
    complement = models.CharField(max_length=64)
    longitude = models.FloatField()
    latitude = models.FloatField()
    ## Armazenar data de criação e atualização (automática pelo Django)
    createad = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Plantation (models.Model):
    farm = models.ForeignKey(Farm,on_delete=models.CASCADE)
    description = models.CharField(max_length=1024)
    plant = models.ForeignKey(Plant,on_delete=models.CASCADE)
    start_season = models.DateField()
    end_season = models.DateField()
    harvest = models.FloatField()
    status = models.IntegerField(default=0)
    ## Armazenar data de criação e atualização (automática pelo Django)
    createad = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Water_Tank (models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    name = models.CharField("Tank Name",max_length=255)
    total_capacity = models.FloatField()
    current_capacity = models.FloatField()
    ## Armazenar data de criação e atualização (automática pelo Django)
    createad = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Plantation_Water_Routine (models.Model):
    plantation = models.ForeignKey(Plantation,on_delete=models.CASCADE)
    period = models.IntegerField()
    programmed_volume_water = models.FloatField()
    ## Armazenar data de criação e atualização (automática pelo Django)
    createad = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Audit_Water_Routine (models.Model):
    routine = models.ForeignKey(Plantation_Water_Routine, on_delete=models.CASCADE)
    date = models.DateTimeField()
    used_water = models.FloatField()
    ## Armazenar data de criação e atualização (automática pelo Django)
    createad = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Climate_History (models.Model):
    farm = models.ForeignKey(Farm,on_delete=models.CASCADE)
    query_date = models.DateTimeField()
    wind_kph = models.FloatField()
    precip_mm = models.FloatField()
    humidity = models.FloatField()
    temp_c = models.FloatField()
    ## Armazenar data de criação e atualização (automática pelo Django)
    createad = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)