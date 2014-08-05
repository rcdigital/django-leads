from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from brz import settings

class ContactEmail:
    def get_verbose_name_of_model(self, model):
        fields = model._meta.get_fields_with_model()
        data = {}
        for index, f in fields:
            data[index.name] = index.verbose_name
        return data

    def convert_to_text(self, model, form):
        fields = self.get_verbose_name_of_model(model)
        email_content = ''
        for f in form:
            if f != 'csrfmiddlewaretoken':
                name = form[ f ]
                verbose_name = fields[ f ]
                email_content += verbose_name+': '+name+";"
        return email_content

    def convert_email_to_array(self, model, form):
        dict_email = {}
        for key in form:
            if key != 'csrfmiddlewaretoken':
                verbose_name = model._meta.get_field_by_name(key)[0].verbose_name
                dict_email[verbose_name] = form[key]
        return dict_email

    def send_email(self, model, form):
        email_content = self.convert_to_text(model, form)
        dict_test = self.convert_email_to_array(model, form)
        html_content = render_to_string('contactmail.html', {'template_data':dict_test} )

        smtpemail = EmailMultiAlternatives(
            'Contact - Site',
            email_content,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_TO,]
        )
        smtpemail.attach_alternative(html_content, "text/html")
        smtpemail.send()
