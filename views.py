# -*- coding: utf8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from brz import settings

from leads.models import TalkWithUs, VisitBuilding, BookBuilding, Register
from leads.forms import TalkWithUsForm, VisitBuildingForm, BookBuildingForm, RegisterForm
from leads.contact import ContactEmail

from leads.feedback_email import FeedbackEmail


def talk_with_us(request):
    if request.method == 'POST':
        form = TalkWithUsForm( request.POST, instance=TalkWithUs() )
        return save_lead(TalkWithUs, request.POST, form)
    else:
         raise Http404

def register(request):
    if request.method == 'POST':
        form = RegisterForm( request.POST, instance=Register() )

        if form.is_valid():
            try:
                form.save()
                feedbackEmail = FeedbackEmail()
                feedbackEmail.send_email(form)
            except Exception:
                return mail_response('false')
            return mail_response('true')
        else:
            return mail_response('false')
    else:
        raise Http404

def save_lead(model, requestForm, form):
    if form.is_valid():
        try:
            form.save()
        except Exception:
            return mail_response('false')



        feedbackEmail = FeedbackEmail()
        feedbackEmail.send_email(form)

        contactLeads = ContactEmail()
        contactLeads.send_email(model, requestForm)

        return mail_response('true')
    else:
        return mail_response('false')


def mail_response(result):
    return HttpResponse(result, mimetype="application/json")
