# -*- coding: utf8 -*-
from import_export import resources
from django.db import models

class BaseLeads(models.Model):
    name = models.CharField('Nome', max_length=258)
    email = models.EmailField('E-mail', max_length=258)
    phone = models.CharField('Telefone', max_length=50 )
    origin_contact = models.CharField('Origem de contato', max_length=258, blank=True)
    created_date = models.DateTimeField('Data de cadastro',auto_now_add=True, blank= True, null= True)
    updated_date = models.DateTimeField(auto_now=True, blank = True, null= True)

class TalkWithUs(BaseLeads):

    CHOICES = (
        ('corretor', 'Corretor'),
        ('pagina','Páginas'),
    )

    age = models.CharField('Idade', max_length=2)
    familiar_rent = models.CharField('Renda Familiar', max_length=100)
    maritial_status = models.CharField('Estado Civil', max_length=100)
    schooling =  models.CharField('Escolaridade', max_length=100)
    house_type = models.CharField('Tipo de residência', max_length=100)
    has_child = models.CharField('Possui filhos?', max_length=100)
    child_number = models.CharField('Quantidade de filhos', max_length=100, null = True, blank = True)
    professional_profile = models.CharField('Perfil Profissional', max_length=100)
    fgts = models.CharField('Possui fgts?', max_length=100)
    consultor_name = models.CharField('Consultor', max_length=100, null = True, blank = True)
    custom_page = models.CharField('Página Direcionada', max_length=100, choices = CHOICES, blank= True ,null= True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Cadastro do Empreendimento'
        verbose_name_plural = 'Cadastro do Empreendimento'

class TalkWithUsResource(resources.ModelResource):
    class Meta:
        model = TalkWithUs

class VisitBuilding(BaseLeads):
    class Meta:
        verbose_name = 'Visite o Empreendimento'
        verbose_name_plural = 'Visite o Empreendimento'
    pass

class BookBuilding(BaseLeads):
    class Meta:
        verbose_name = 'Reserve'
        verbose_name_plural = 'Reserve'
    pass

class Register(BaseLeads):
    city = models.CharField('Cidade', max_length=100, null = True, blank = True) 

    class Meta:
        verbose_name = 'Cadastre-se gratuitamente'
        verbose_name_plural = 'Cadastre-se gratuitamente'
    pass
