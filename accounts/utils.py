# password
import re
from django.contrib import messages
from django.contrib.messages import constants

#email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.core.exceptions import ValidationError

''''''
def password_is_valid(request, password, confirm_password):
    if len(password) < 6:
        messages.add_message(request, constants.ERROR, 'Sua senha deve conter 6 ou mais caractertes')
        return False
    
    if not password == confirm_password:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem!')
            return False
        
    if not re.search('[A-Z]', password):
            messages.add_message(request, constants.ERROR, 'Sua senha não contem letras maiúsculas')
            return False
        
    if not re.search('[a-z]', password):
            messages.add_message(request, constants.ERROR, 'Sua senha não contem letras minúsculas')
            return False
        
    if not re.search('[1-9]', password):
            messages.add_message(request, constants.ERROR, 'Sua senha não contém números')
            return False
    return True


'''
def email_html(path_template: str, assunto: str, para: list, **kwargs) -> dict:
        
        html_content = render_to_string(path_template, kwargs)
        text_content = strip_tags(html_content) # REMOVE AS TAGS HTML DO EMAIL
        
        email = EmailMultiAlternatives(assunto, text_content, settings.EMAIL_HOST_USER, para)
        
        email.attach_alternative(html_content, "text/html")
        email.send()
        return {'status': 1}
'''

# VALIDA EMAIL

def email_is_valid(email):
    regex = re.compile(
            r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
    )  # noqa: E501
    return bool(re.fullmatch(regex, email))




# VALIDA SENHA

def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError((
            'No mínimo 8 caracteres, '
            'possuir pelo menos uma letra minuscula, '
            'uma letra maiúscula e um número'
        ),
            code='invalid'
        )