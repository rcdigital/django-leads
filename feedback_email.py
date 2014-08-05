from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from brz import settings

class FeedbackEmail:
    def send_email(self, data):
        name = data.data.get('name','')
        email = data.data.get('email','')
        url = 'http://brzempreendimentos.com'
        emailcontent = '' \
        + ( 'Nome: %s \n' % name ) \
        + ( 'E-mail: %s \n' % email )
        html_content = render_to_string('feedback_email.html', {
            'name': name,
            'email': email,
            'url': url,
        })
        smtpemail = EmailMultiAlternatives(
            'BRZ Empreendimentos - Obrigado por se cadastrar no nosso site',
            emailcontent,
            settings.EMAIL_HOST_USER,
            #TODO - Uncomment to enable email sending to recipients
            #form.data.get('destination'),
            [email]
        )
        smtpemail.attach_alternative(html_content, "text/html")
        smtpemail.send()
